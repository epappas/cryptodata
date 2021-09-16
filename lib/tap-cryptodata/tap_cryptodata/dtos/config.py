from dataclasses import dataclass
from typing import Any, List

@dataclass
class ConfigDto:
    stream_name: str
    stream_version: str
    source_name: str
    source_type: str
    in_schema: Any
    url: str
    data: dict = {}
    params: dict = {}
    headers: dict = {}
    key_properties: List = ["ticker_id", "base", "target"]
    bookmark_properties: List = ["x-stream_name", "x-source_name", "x-source_type"]
