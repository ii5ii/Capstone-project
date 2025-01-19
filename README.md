
source .venv/bin/activate //mac\
pip install django\
django-admin startproject LittleLemon .\
python manage.py startapp Restaurant

Register the App in settings.py\
INSTALLED_APPS = [\
  "Restaurant",\
]

link github\
git init\
git add .\
git commit -m "initial commit"\
git checkout -b test-branch\
git remote -v\
git push -u origin test-branch\
