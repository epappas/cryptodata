#!/usr/bin/env python3
"""
tap streaming data
"""

import singer

from .pairs import fetch_betconix_v1_pairs
from .utils import load_schema, LOGGER
from .config_dto import ConfigDto


STATE = {}
REQUIRED_CONFIG_KEYS = []

RESOURCES = {
    'pairs': [{
        'sync_function': fetch_betconix_v1_pairs,
        'sub_streams': [],
        'config': {
            'stream_name': "betconix_v1_pairs",
            'stream_version': "v1",
            'source_name': "betconix",
            'source_type': "CEX_API",
            'url': "https://betconix.com/api/v2/pairs",
            'data': {},
            'params': {},
            'headers': {},
            'in_schema': load_schema("betconix_v1_pairs"),
            'key_properties': ["ticker_id", "base", "target"],
            'bookmark_properties': ["x-stream_name", "x-source_name", "x-source_type"],
            'xparams': {}
        }
    }]
}

def do_sync(config = {}, state = {}):
    """
    Execute the sync logic
    """

    LOGGER.info("Starting sync")

    for _, streams in RESOURCES.items():
        for stream in streams:
            sync_function = stream['sync_function']

            conf = {}
            conf.update(stream['config'])
            if conf['stream_name'] in config:
                conf.update(config[conf['stream_name']])

            sync_function(ConfigDto(
                stream_name = conf['stream_name'],
                stream_version = conf['stream_version'],
                source_name = conf['source_name'],
                source_type = conf['source_type'],
                in_schema = conf['in_schema'],
                url = conf['url'],
                data = conf['data'],
                params = conf['params'],
                headers = conf['headers'],
                key_properties = conf['key_properties'],
                bookmark_properties = conf['bookmark_properties'],
                xparams = conf['xparams'],
            ), state=state)

    LOGGER.info("Sync complete")


def main():
    args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)

    if args.state:
        STATE.update(args.state)

    do_sync(args.config, args.state)

if __name__ == '__main__':
    main()
