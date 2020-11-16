import functools
import json

import aiohttp
from aiohttp_apispec import response_schema
from aiohttp_jinja2 import template

from .models import Cars
from .schemas import CarResponseSchema

pretty_json = functools.partial(json.dumps, indent=4)


@template('index.html')
async def handle(request):
    site_name = request.app['config'].get('site_name')
    return {
        'status': 'success',
        'site_name': site_name
    }


@response_schema(CarResponseSchema(many=True), 200)
async def cars_list(request):
    cars_qs = await Cars.query.gino.all()
    cars_schema = CarResponseSchema(many=True)
    cars_json, errors = cars_schema.dump(cars_qs)
    return aiohttp.web.json_response({'jokes': cars_json}, dumps=pretty_json)


@response_schema(CarResponseSchema(), 200)
async def car_detail(request):
    car_id = int(request.match_info['id'])
    car = await Cars.get(id=2)

    if car is None:
        raise aiohttp.web.HTTPNotFound()

    car_schema = CarResponseSchema()
    car_json, errors = car_schema.dump(car)

    return aiohttp.web.json_response(car_json, dumps=pretty_json)
