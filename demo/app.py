import asyncpg
import aiohttp_jinja2
import jinja2
from aiohttp import web

from . import api
from .routes import setup_routes


async def init_db(database_uri: str):
    db = api.models.db
    await db.set_bind(database_uri)
    await db.gino.create_all()


async def create_app(config: dict):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    setup_routes(app)

    await init_db(config['database_uri'])
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)

    return app


async def on_start(app):
    config = app['config']
    app['db'] = await asyncpg.create_pool(
        dsn=config['database_uri']
    )


async def on_shutdown(app):
    await app['db'].close()

