#!/bin/sh

set -e

export PATH="/app/.venv/bin:$PATH"

. /app/.venv/bin/activate

python /app/todo_core/manage.py runserver "$WEB_HOST":8080
    
    