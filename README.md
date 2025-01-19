
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

cannot pull,merge "There isn’t anything to compare" cuz\
local test-branch has a completely independent history\because didn't start project by cloning the remote repository\
git fetch origin\
git checkout test-branch\
git rebase origin/main\
git push -f origin test-branch\
go back to github Create and Merge Pull Request\


