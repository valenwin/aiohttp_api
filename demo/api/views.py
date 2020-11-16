from aiohttp import web
import json


async def handle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj),
                        status=200)
