#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="tap-cryptodata",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Evangelos Pappas",
    url="http://singer.io",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    py_modules=["tap_cryptodata"],
    python_requires='>=3.6,<4',
    install_requires=[
        "singer-python>=5.12.1",
        "requests>=2.20.0",
        "backoff>=1.8.0",
        'web3==4.7.2',
        'eth-utils==2.0.0',
        'eth-abi==2.1.1',
        'click==8.0.1',
        'ethereum-dasm==0.1.4',
        'base58',
    ],
    extras_require={
        'dev': [
            'pytest~=4.3.0'
        ]
    },
    entry_points="""
    [console_scripts]
    tap-cryptodata=tap_cryptodata:main
    """,
    # packages=["tap_cryptodata"],
    packages=find_packages(exclude=['tests*']),
    package_data = {
        "schemas": ["tap_cryptodata/schemas/*.json"]
    },
    include_package_data=True,

    project_urls={
        'Bug Reports': 'https://github.com/epappas/cryptodata/issues',
        'Source': 'https://github.com/epappas/cryptodata',
    },
)
