from .api import views


def setup_routes(app):
    app.router.add_route('GET', '/', views.handle)
    app.router.add_route('GET', '/api/cars', views.cars_list)
    app.router.add_route('GET', r'/api/cars/{id:\d+}', views.car_detail)
