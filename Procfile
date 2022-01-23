web: gunicorn blog_project.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
python manage.py migrate
python manage.py collectstatic