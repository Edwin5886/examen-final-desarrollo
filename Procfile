release: python init_production.py && python manage.py collectstatic --noinput
web: gunicorn Final.wsgi:application --bind 0.0.0.0:$PORT --log-level info