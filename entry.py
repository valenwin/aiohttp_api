import aiohttp
import argparse
from demo import create_app
from demo.settings import load_config

parser = argparse.ArgumentParser(description='Demo Project')
parser.add_argument('-c', '--config', type=argparse.FileType('r'),
                    help='Path to configuration file')

args = parser.parse_args()

app = create_app(config=load_config(args.config))

if __name__ == '__main__':
    aiohttp.web.run_app(app)
