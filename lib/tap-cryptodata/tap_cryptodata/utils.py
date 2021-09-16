import os
import requests
import backoff
import singer

from typing import Iterator
from requests import Response
from singer import utils

LOGGER = singer.get_logger()
SESSION = requests.Session()

class ReqException(Exception):
    pass

def get_abs_path(path) -> str:
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)

def load_schema(entity):
    return utils.load_json(get_abs_path("schemas/{}.json".format(entity)))

@backoff.on_exception(backoff.expo,
                      (requests.exceptions.RequestException),
                      max_tries=5,
                      giveup=lambda e: e.response is not None and 400 <= e.response.status_code < 500, # pylint: disable=line-too-long
                      factor=2)
def request(url, method="GET", headers={}, params={}, data={}) -> Response:
    req = requests.Request(method, url, headers, params=params, data=data).prepare()
    LOGGER.info("{} {}".format(method, req.url))

    response = SESSION.send(req)
    if response.status_code >= 400:
        error = "Error making request to GitLab API: {} {} [{} - {}]".format(method, req.url, response.status_code, response.content)
        LOGGER.critical(error)
        raise ReqException(error)

    return response


def fetch(url, headers={}, params={}, data={}) -> Iterator[Response]:
    with request(url, headers=headers, params=params, data=data) as response:
        for row in response.json():
            yield row
