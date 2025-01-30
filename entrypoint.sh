#!/bin/bash

set -e

until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  echo "Waiting for database at $DB_HOST:$DB_PORT..."
  sleep 2
done

cd todo_core/

pipenv run ./manage.py makemigrations
pipenv run  ./manage.py migrate --noinput
pipenv run ./manage.py runserver "$WEB_HOST":8080
    
