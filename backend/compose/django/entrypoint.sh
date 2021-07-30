#!/bin/bash

# apply migrations
python manage.py migrate

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Start server
echo "Starting server"

daphne -b 0 config.asgi:application
