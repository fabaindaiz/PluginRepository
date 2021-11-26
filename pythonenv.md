# Comandos para instalar django

    python -m venv env
    env\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt

# Comandos para correr django

    python manage.py makemigrations PluginBackend Web
    python manage.py migrate
    python manage.py loaddata PluginBackend/json/data.json
    python manage.py createsuperuser
    python manage.py runserver