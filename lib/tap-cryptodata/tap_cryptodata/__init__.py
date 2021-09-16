#!/usr/bin/env python3

from logging import config
import singer
import singer.bookmarks as bookmarks
import singer.metrics as metrics
from singer import metadata

from .pairs import fetch_betconix_v1_pairs
from .utils import load_schema, LOGGER
from .config import ConfigDto


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
        }
    }]
}

def do_sync():
    LOGGER.info("Starting sync")

    for name, streams in RESOURCES.items():
        for stream in streams:
            conf = stream['config']
            stream['sync_function'](ConfigDto(
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
            ), state={})

    LOGGER.info("Sync complete")


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)

    if args.state:
        STATE.update(args.state)

    do_sync()

if __name__ == '__main__':
    main()
