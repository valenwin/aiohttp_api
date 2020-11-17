import argparse
import asyncio

import aiohttp
import aioreloader

from demo import create_app
from demo.settings import load_config

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('Library uvloop isn\'t available.')

parser = argparse.ArgumentParser(description='Demo Project')
parser.add_argument('-c', '--config', type=argparse.FileType('r'),
                    help='Path to configuration file')
parser.add_argument('--host',
                    help='host to listen', default='0.0.0.0')
parser.add_argument('--port',
                    help='port to accept connections', default=8080)
parser.add_argument('--reload',
                    action='store_true',
                    help='auto-reload code on change')

args = parser.parse_args()

app = create_app(config=load_config(args.config))

if args.reload:
    print('Start with code reload')
    app = aiohttp.web.Application()
    aioreloader.start()

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)
