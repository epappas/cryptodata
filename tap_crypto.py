import singer
import uuid
from datetime import datetime, timezone

import requests

url = "https://betconix.com/api/v2/pairs"
payload={}
headers = {}

now = datetime.now(timezone.utc).isoformat()
key_properties = ["ticker_id", "base", "target"]
bookmark_properties = ["x-stream_name", "x-source_name", "x-source_type"]
schema = {
    'additionalProperties': False,
    'properties': {
        'ticker_id': { 'type': "string" },
        'base': { 'type': "string" },
        'target': { 'type': "string" },
        # --- Meta ---
        'x-batch_id': { 'type': "string" },
        'x-stream_name': { 'type': "string" },
        'x-stream_version': { 'type': "string" },
        'x-source_name': { 'type': "string" },
        'x-source_type': ["CEX_API"],
        'x-source_uri': { 'type': "string", 'format': "uri-reference" },
        'x-timestamp': { 'type': "string", 'format': "date-time" },
        'x-tap_version': { 'type': "string" },
    },
}

with requests.request("GET", url, headers=headers, data=payload) as response:
    base = {
        'x-batch_id': str(uuid.uuid4()),
        'x-stream_name': "betconix_v1_pairs",
        'x-stream_version': "v1",
        'x-source_name': "betconix",
        'x-source_type': "CEX_API",
        'x-source_uri': url,
        'x-timestamp': now,
        'x-tap_version': "tap_crypto@0.0.1",
    }

    singer.write_schema(base["x-stream_name"], schema, key_properties)
    singer.write_version(base["x-stream_name"], base["x-stream_version"])

    for pair in response.json():
        record = dict()
        record.update(base)
        record.update(pair)
        singer.write_records(base["x-stream_name"], [record])

    singer.write_state({
        'x-stream_name': base["x-stream_name"],
        'latest-batch_id': base["x-batch_id"],
        'latest-update': now,
        'latest-tap_version': base["x-tap_version"],
    })
