"""Setup.py for the Astronomer sample Airflow provider package. Built from datadog provider package for now."""

from setuptools import find_packages, setup

"""Perform the package airflow-provider-sample setup."""
setup(
    name='airflow-provider-sample',
    version="0.0.1",
    description='',
    long_description="",
    long_description_content_type='text/markdown',
    entry_points={
        "apache_airflow_provider": [
            "provider_info=sample_provider.__init__:get_provider_info"
        ]
    },
    license='Apache License 2.0',
    packages=['sample_provider', 'sample_provider.hooks',
              'sample_provider.sensors', 'sample_provider.operators'],
    install_requires=['apache-airflow>=1.10.15'],
    setup_requires=['setuptools', 'wheel'],
    python_requires='~=3.7',
)
