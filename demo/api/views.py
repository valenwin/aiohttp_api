import functools
import json

from aiohttp import ClientSession, web
from aiohttp_apispec import response_schema, request_schema
from aiohttp_jinja2 import template
from asyncpg import UniqueViolationError
from marshmallow import ValidationError

from .models import Cars
from .schemas import CarResponseSchema, CarRequestSchema, DeleteCarResponseSchema

pretty_json = functools.partial(json.dumps, indent=4)


@template('index.html')
async def handle(request):
    site_name = request.app['config'].get('site_name')
    return {
        'status': 'success',
        'site_name': site_name
    }


@response_schema(CarResponseSchema(many=True), 200)
async def cars_list(request: web.Request):
    cars_qs = await Cars.query.gino.all()
    cars_schema = CarResponseSchema(many=True)
    cars_json = cars_schema.dump(cars_qs)
    return web.json_response({'cars': cars_json},
                             dumps=pretty_json)


@response_schema(CarResponseSchema(), 200)
async def car_detail(request: web.Request):
    car_id = int(request.match_info['id'])
    car = await Cars.get(car_id)

    car_schema = CarResponseSchema()
    car_json = car_schema.dump(car)

    return web.json_response(car_json,
                             dumps=pretty_json)


@response_schema(CarResponseSchema())
async def car_create(request: web.Request):
    car_schema = CarResponseSchema()

    async with ClientSession() as session:
        car = None
        try:
            car_schema.load({
                'year': request.query['year'],
                'vin_code': request.query['vin_code'],
            })
            car = await Cars.create(
                producer=request.query['producer'],
                model=request.query['model'],
                year=int(request.query['year']),
                color=request.query['color'],
                vin_code=request.query['vin_code']
            )
        except ValidationError as err:
            print(err.messages)
        except UniqueViolationError:
            print("Vin-code should be unique")

    car_json = car_schema.dump(car)

    return web.json_response(car_json,
                             dumps=pretty_json,
                             status=201)


@request_schema(CarRequestSchema())
@response_schema(CarResponseSchema(), 200)
async def car_update(request: web.Request):
    car_id = int(request.match_info['id'])
    new_color = request.query['color']

    car = await Cars.get(car_id)

    await car.update(color=new_color).apply()

    car_schema = CarResponseSchema()
    car_json = car_schema.dump(car)

    return web.json_response(car_json,
                             dumps=pretty_json)


@response_schema(DeleteCarResponseSchema(), code=204)
async def car_delete(request: web.Request):
    car_id = int(request.match_info['id'])
    car = await Cars.get(car_id)

    await car.delete()

    return web.json_response(
        {'Message': 'Car was successfully deleted from db.'},
        dumps=pretty_json,
        status=204)


@response_schema(CarResponseSchema(), 200)
async def car_filter(request: web.Request):
    producer = request.match_info['producer']
    cars_qs = await Cars.query.where(Cars.producer == producer).gino.all()

    cars_schema = CarResponseSchema(many=True)
    cars_json = cars_schema.dump(cars_qs)
    return web.json_response({'cars': cars_json},
                             dumps=pretty_json)
