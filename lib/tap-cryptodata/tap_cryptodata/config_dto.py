from dataclasses import dataclass, field
from typing import Any, List

@dataclass
class ConfigDto:
    stream_name: str
    stream_version: str
    source_name: str
    source_type: str
    in_schema: Any
    url: str
    data: dict = field(default_factory=dict)
    params: dict = field(default_factory=dict)
    headers: dict = field(default_factory=dict)
    key_properties: list = field(default_factory=list)
    bookmark_properties: list = field(default_factory=list)
    xparams: dict = field(default_factory=dict)
