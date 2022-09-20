#!/bin/bash
# drop and re-recreate schema "public" for localhost (dev)
psql postgresql://postgres:pw20220501@localhost:5432/django_app_dev -c "drop schema public cascade; create schema public;"
python manage.py makemigrations
python manage.py migrate
