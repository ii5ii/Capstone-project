
source .venv/bin/activate //mac
pip install django
django-admin startproject LittleLemon .
python manage.py startapp Restaurant

Register the App in settings.py
INSTALLED_APPS = [
  "Restaurant",
]
