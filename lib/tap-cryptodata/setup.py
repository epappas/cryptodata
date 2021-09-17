#!/usr/bin/env python3

from setuptools import setup

setup(
    name="tap-cryptodata",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Evangelos Pappas",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_cryptodata"],
    install_requires=[
        "singer-python>=5.12.1",
        "requests>=2.20.0",
        "backoff>=1.8.0"
    ],
    entry_points="""
    [console_scripts]
    tap-cryptodata=tap_cryptodata:main
    """,
    packages=["tap_cryptodata"],
    package_data = {
        "schemas": ["tap_cryptodata/schemas/*.json"]
    },
    include_package_data=True,
)
