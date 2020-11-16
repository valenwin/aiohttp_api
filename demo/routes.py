from .api import views


def setup_routes(app):
    app.router.add_route('GET', '/', views.handle)
    app.router.add_route('GET', '/api/cars', views.cars_list)
    app.router.add_route('GET', r'/api/cars/{id:\d+}', views.car_detail)
    app.router.add_route('POST', '/api/cars', views.car_create)
    app.router.add_route('PUT', r'/api/cars/{id:\d+}', views.car_update)
    app.router.add_route('DELETE', r'/api/cars/{id:\d+}', views.car_delete)
    app.router.add_route('GET', r'/api/cars/filter={producer}', views.car_filter)
