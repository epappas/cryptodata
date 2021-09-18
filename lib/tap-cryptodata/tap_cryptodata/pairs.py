from typing import Dict
import uuid
import singer
import singer.metrics as metrics

from .config_dto import ConfigDto
from .utils import fetch

def fetch_betconix_v1_pairs(config: ConfigDto, state={}) -> Dict:
    url = config.url
    extraction_time = singer.utils.now()
    now = extraction_time.isoformat()
    batch_id = str(uuid.uuid4())
    tap_version = "tap_crypto@0.1.0"
    base = {
        'x-batch_id': batch_id,
        'x-stream_name': config.stream_name,
        'x-stream_version': config.stream_version,
        'x-source_name': config.source_name,
        'x-source_type': config.source_type,
        'x-source_uri': config.url,
        'x-timestamp': now,
        'x-tap_version': tap_version,
    }

    singer.write_schema(config.stream_name, config.in_schema, config.key_properties, config.bookmark_properties)
    # singer.write_version(config.stream_name, config.stream_version)

    with metrics.record_counter('pairs') as counter:
        for row in fetch(url, headers=config.headers, params=config.params, data=config.data):
            record = dict()
            record.update(base)
            record.update(row)
            singer.write_record(config.stream_name, record, time_extracted=extraction_time)
            counter.increment()

    singer.write_state({
        'x-stream_name': config.stream_name,
        'latest-batch_id': batch_id,
        'latest-update': now,
        'latest-tap_version': tap_version,
    })

    return state

