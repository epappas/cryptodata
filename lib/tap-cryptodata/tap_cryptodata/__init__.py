#!/usr/bin/env python3

import argparse
import os
import json
import collections
import requests
import singer
import singer.bookmarks as bookmarks
import singer.metrics as metrics
from singer import metadata

from .pairs import get_all_pairs
from .utils import load_schema, LOGGER


STATE = {}
REQUIRED_CONFIG_KEYS = []

RESOURCES = {
    'pairs': [{
        'sync_function': get_all_pairs,
        'sub_streams': [],
        'config': {
            'stream_name': "betconix_v1_pairs",
            'stream_version': "v1",
            'source_name': "betconix",
            'source_type': "CEX_API",
            'url': "https://betconix.com/api/v2/pairs",
            'payload': {},
            'headers': {},
            'in_schema': load_schema("betconix_v1_pairs"),
            'key_properties': ["ticker_id", "base", "target"],
            'bookmark_properties': ["x-stream_name", "x-source_name", "x-source_type"],
        }
    }]
}

def do_sync():
    LOGGER.info("Starting sync")

    gids = list(filter(None, CONFIG['groups'].split(' ')))
    pids = list(filter(None, CONFIG['projects'].split(' ')))

    for resource, config in RESOURCES.items():
        singer.write_schema(resource, config['schema'], config['key_properties'])

    for gid in gids:
        sync_group(gid, pids)

    if not gids:
        # When not syncing groups
        for pid in pids:
            sync_project(pid)

    LOGGER.info("Sync complete")


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)

     # TODO: Address properties that are required or not
    args = utils.parse_args(["private_token", "projects", "start_date"])

    CONFIG.update(args.config)

    if args.state:
        STATE.update(args.state)

    do_sync()

if __name__ == '__main__':
    main()
