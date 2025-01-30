#!/bin/bash

set -e

until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  echo "Waiting for database..."
  sleep 2
done

python manage.py makemigrations
python manage.py migrate --noinput

python manage.py collectstatic --noinput

exec python manage.py runserver "":8080
    
