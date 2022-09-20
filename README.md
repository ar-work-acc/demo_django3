# Django demo app

This is just a demo app (not maintained anymore).

## Dependencies

Use Python 3.10.  
Use Django 3.2 LTS.  
Use Django REST framework 3.13.1.

## Project structure and apps:

TODOs

1. Folder names starting with and underscore indicates it's not used or is not a
   package.
2. Use Gunicorn for synchronous requests; Daphne for websocket requests (2
   containers).

## Coverage

```
$ coverage run --source=. manage.py test
$ coverage report
$ coverage html
```

## Install PostgreSQL driver package:

```
$ sudo apt install libpq-dev
```

Shows:

The following packages have unmet dependencies:  
libpq-dev : Depends: libpq5 (= 12.11-0ubuntu0.20.04.1) but 14.3-1.pgdg20.04+1 is
to be installed

To fix the problem:

```
$ sudo apt install libpq5=12.11-0ubuntu0.20.04.1
```

Then install it again.

You can also obtain a stand-alone package, not requiring a compiler or external
libraries, by installing the psycopg2-binary package from PyPI (just use this):

```
$ pip install psycopg2-binary
```

## Docker, Docker Compose:

In folder "mysite":

- .dockerignore: remember to list those files that shouldn't be copied to the
  container
- docker-compose.yml: depends_on does not wait for the DB service to become
  ready; also use "nginx" folder to build images.
- Dockerfile: so we use "wait-for-it.sh" to wait for PostgreSQL to become ready!
- requirement.txt: for container; dependencies in this file must include a
  specific version! (don't install those in requirements.local.txt)
- run.sh: container CMD shell script; list commands here so that we can wait for
  it
- wait-for-it.sh: wait for the service to become ready
  (https://docs.docker.com/compose/startup-order/ ,
  https://github.com/vishnubob/wait-for-it)

Scripts starting with an underscore is for local develpment only:

- \_build_compose.sh: use this to run docker compose; it builds and clears old
  images automatically
- \_recreate_schema.sh: for local development only (drop and create public
  schema)
- \_pip_reinstall.sh: when you need a clean re-install of your venv

Will start Nginx service on port 8001 (with DEBUG = False).

## Django, custom settings

1. Use "?page=2&pageSize=3" to get the page you want (custom pagination class:
   'snippets.pagination.CustomPagination')

## Web sockets

https://nginx.org/en/docs/http/websocket.html  
A more sophisticated example in which a value of the “Connection” header field
in a request to the proxied server depends on the presence of the “Upgrade”
field in the client request header:

```
http {
    map $http_upgrade $connection_upgrade {
        default upgrade;
        ''      close;
    }

    server {
        ...

        location /chat/ {
            proxy_pass http://backend;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection $connection_upgrade;
        }
    }
```

By default, the connection will be closed if the proxied server does not
transmit any data within 60 seconds. This timeout can be increased with the
proxy_read_timeout directive. Alternatively, the proxied server can be
configured to periodically send WebSocket ping frames to reset the timeout and
check if the connection is still alive.
