#!/bin/sh

echo "Running DB migrations..."
flask db upgrade

echo "Starting Gunicorn server..."
exec gunicorn -w 4 -b 0.0.0.0:5000 run:app
