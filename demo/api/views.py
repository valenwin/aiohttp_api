from aiohttp_jinja2 import template


@template('index.html')
async def handle(request):
    site_name = request.app['config'].get('site_name')
    return {
        'status': 'success',
        'site_name': site_name
    }
