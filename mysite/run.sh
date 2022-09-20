#!/bin/bash
# This script is for our Docker container server (with initialization):
python manage.py migrate
python manage.py createsuperuser --noinput --email meowfish.org@gmail.com
python manage.py collectstatic --noinput

#gunicorn mysite.wsgi:application --bind=0.0.0.0:8000 --workers=4
daphne -b 0.0.0.0 -p 8000 mysite.asgi:application
