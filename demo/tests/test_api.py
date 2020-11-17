import pytest
from aiohttp import web

from demo.api import views


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    app.router.add_route('GET', '/api/cars', views.cars_list)
    app.router.add_route('GET', r'/api/cars/{id:\d+}', views.car_detail)
    app.router.add_route('POST', '/api/cars', views.car_create)
    app.router.add_route('PUT', r'/api/cars/{id:\d+}', views.car_update)
    app.router.add_route('DELETE', r'/api/cars/{id:\d+}', views.car_delete)
    return loop.run_until_complete(aiohttp_client(app))


async def test_car_create(cli):
    post_resp = await cli.post(
        '/api/cars?producer=Toyota&model=Corolla&year=2019&color=Green&vin_code=JN1WNYD21U0000007')
    assert post_resp.status == 201


async def test_cars_list(cli):
    get_resp = await cli.get('/api/cars')
    assert get_resp.status == 200


async def test_car_detail(cli):
    get_resp = await cli.get('/api/cars/1')
    assert get_resp.status == 200


async def test_car_detail_404(cli):
    get_resp = await cli.get('/api/cars/200')
    assert get_resp.status == 404


async def test_car_update(cli):
    put_resp = await cli.put(
        '/api/cars/1',
        json={'color': 'white'})
    assert put_resp.status == 200


async def test_car_delete(cli):
    del_resp = await cli.delete('/api/cars/1')
    assert del_resp.status == 204


async def test_car_delete_404(cli):
    del_resp = await cli.delete('/api/cars/200')
    assert del_resp.status == 404
