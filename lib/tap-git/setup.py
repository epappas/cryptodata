#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-git",
    version="0.1.0",
    description="Singer.io tap for extracting data from git repos",
    author="Evangelos Pappas <epappas@evalonlabs.com>",
    url="https://github.com/epappas",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_git"],
    install_requires=[
        'singer-python>=5.12.1',
        'requests>=2.20.0'
        'GitPython>=3.1.14'
    ],
    entry_points="""
    [console_scripts]
    tap-git=tap_git:main
    """,
    packages=["tap_git"],
    package_data = {
        "schemas": ["tap_git/schemas/*.json"]
    },
    include_package_data=True,
)
