FROM python:3.10

LABEL author="meowfish.org@gmail.com"

# environment variables:
# DJANGO_ENV: development, staging, production
ENV DJANGO_ENV production
# https://docs.python.org/3/using/cmdline.html#cmdoption-u
# (after Python 3.7, this is unnecessary?)
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_USERNAME archvile
ENV DJANGO_SUPERUSER_PASSWORD pw20220501

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x *.sh

EXPOSE 8000

# all manage.py commands goes into "run.sh" (so that we can wait for postgres to be ready first):
CMD ["./wait-for-it.sh", "postgres:5432", "--", "./run.sh"]
