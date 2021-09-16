import argparse
import os
import json
import collections
import requests
import singer
import singer.bookmarks as bookmarks
import singer.metrics as metrics

from singer import metadata

def sync_branches(project):
    url = get_url("branches", project['id'])
    with Transformer(pre_hook=format_timestamp) as transformer:
        for row in gen_request(url):
            row['project_id'] = project['id']
            flatten_id(row, "commit")
            transformed_row = transformer.transform(row, RESOURCES["branches"]["schema"])
            singer.write_record("branches", transformed_row, time_extracted=utils.now())



def get_all_pairs(schemas, repo_path, state, mdata):
    # https://developer.github.com/v3/repos/comments/
    # updated_at? incremental
    # 'https://api.github.com/repos/{}/comments?sort=created_at&direction=desc'.format(repo_path)
    bookmark_value = get_bookmark(state, repo_path, "pairs", "since")
    if bookmark_value:
        bookmark_time = singer.utils.strptime_to_utc(bookmark_value)
    else:
        bookmark_time = 0

    with metrics.record_counter('pairs') as counter:
        for response in authed_get_all_pages(
                'pairs',
                'https://api.github.com/repos/{}/comments?sort=created_at&direction=desc'.format(repo_path)
        ):
            pairs = response.json()
            extraction_time = singer.utils.now()
            for r in pairs:
                r['_sdc_repository'] = repo_path

                # skip records that haven't been updated since the last run
                # the GitHub API doesn't currently allow a ?since param for pulls
                # once we find the first piece of old data we can return, thanks to
                # the sorting
                if bookmark_time and singer.utils.strptime_to_utc(r.get('updated_at')) < bookmark_time:
                    return state

                # transform and write release record
                with singer.Transformer() as transformer:
                    rec = transformer.transform(r, schemas, metadata=metadata.to_map(mdata))
                singer.write_record('pairs', rec, time_extracted=extraction_time)
                singer.write_bookmark(state, repo_path, 'pairs', {'since': singer.utils.strftime(extraction_time)})
                counter.increment()

    return state
