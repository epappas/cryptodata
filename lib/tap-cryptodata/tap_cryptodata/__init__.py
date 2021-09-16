#!/usr/bin/env python3

from logging import config
import singer
import singer.bookmarks as bookmarks
import singer.metrics as metrics
from singer import metadata

from .pairs import fetch_betconix_v1_pairs
from .utils import load_schema, LOGGER
from .dtos.config import ConfigDto


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

    for streams in RESOURCES.items():
        for stream in streams:
            stream.sync_function(ConfigDto(
                stream_name = stream.config['stream_name'],
                stream_version = stream.config['stream_version'],
                source_name = stream.config['source_name'],
                source_type = stream.config['source_type'],
                in_schema = stream.config['url'],
                url = stream.config['data'],
                data = stream.config['params'],
                params = stream.config['headers'],
                headers = stream.config['in_schema'],
                key_properties = stream.config['key_properties'],
                bookmark_properties = stream.config['bookmark_properties'],
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
