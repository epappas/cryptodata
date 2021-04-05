# Meltano & Docker Compose

*[This file](https://gitlab.com/meltano/files-docker-compose/-/blob/master/bundle/README.md) has been added to your project for convenience and reference only. Feel free to delete it.*

## Getting started

1. Start the `meltano-ui` service (and any others) in the background:

    ```bash
    docker-compose up -d
    ```

1. Open Meltano UI at <http://localhost:5000>.

### Helpful commands

- `docker-compose exec meltano-ui /bin/bash`: Get a bash shell inside your Meltano container.
- `docker-compose exec meltano-ui meltano {subcommand}`: Run a [`meltano` CLI command](https://meltano.com/docs/command-line-interface.html) inside your container.
- `docker-compose logs`: See all logs.
- `docker-compose logs {service}`: See logs for a particular service, e.g. `meltano-ui`.

## Optional services

If these services are not relevant to you, feel free to delete their commented sections.

### Airflow

If you are using the [Airflow orchestrator](https://meltano.com/docs/orchestration.html) and would like to run it using Docker Compose, follow these steps:

1. Uncomment the `airflow-webserver` and `airflow-scheduler` services.
1. Start the new services:

    ```bash
    docker-compose up -d
    ```

1. Open the Airflow web interface at <http://localhost:8080>.

## Production usage

A `docker-compose.prod.yml` file is included that represents a [production-grade](https://meltano.com/docs/production.html) setup of a [containerized Meltano project](https://meltano.com/docs/containerization.html).

If this is not relevant to you, feel free to delete it.

### Dependencies

The production configuration depends on a `Dockerfile` being present in your project.

If you haven't already, add the appropriate `Dockerfile` and `.dockerignore` files to your project by adding the [`docker` file bundle](https://gitlab.com/meltano/files-docker):

```bash
meltano add files docker
```

### Usage

Please ensure you do the following before deploying to production:

1. If you are using the [Airflow orchestrator](#airflow) and would like to run it using Docker Compose, uncomment the Airflow services, network, and volume, and add `psycopg2` to `airflow`'s `pip_url` in `meltano.yml` as described in the ["Deployment in Production" guide](https://meltano.com/docs/production.html#airflow-orchestrator). If not, feel free to delete the commented sections.
1. Change the database password for `meltano-system-db` (and `airflow-metadata-db`): look for `# CHANGE ME`.
1. Update the database connection URIs under `x-meltano-env` (and `x-airflow-env`) to reflect the changed passwords.
1. Add any environment variables from `.env` and your local environment that are needed for production under `x-meltano-env`.
1. Change the image name and tag under `x-meltano-image` to something that makes sense for your project.
1. Start the services in the background:

    ```bash
    docker-compose -f docker-compose.prod.yml up -d
    ```

If you've made changes to your project and need to rebuild your project-specific image, run `docker-compose -f docker-compose.prod.yml up -d --build`.
