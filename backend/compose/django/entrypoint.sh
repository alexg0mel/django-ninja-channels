#!/bin/bash

# apply migrations
python manage.py migrate

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
#gunicorn -w 2 -b :5000 config.wsgi:application --timeout=55
# or need asgi ???
