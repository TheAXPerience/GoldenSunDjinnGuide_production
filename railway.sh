python djinnguide/manage.py makemigrations && python djinnguide/manage.py migrate && python djinnguide/manage.py runscript populate_db && python djinnguide/manage.py runscript populate_categories && cd djinnguide && gunicorn --bind 0.0.0.0:8000 djinnguide.wsgi
python -m http.server $PORT