pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver &
uwsgi --http :8000 --module music_app.wsgi
