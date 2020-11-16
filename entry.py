import argparse

import aiohttp
import aioreloader

from demo import create_app
from demo.settings import load_config

parser = argparse.ArgumentParser(description='Demo Project')
parser.add_argument('-c', '--config', type=argparse.FileType('r'),
                    help='Path to configuration file')
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
    aiohttp.web.run_app(app)
