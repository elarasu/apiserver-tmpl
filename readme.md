# django-apiserver

Very opinionated api server. Comes with the following features 
   * django-rest-framework

Usage:

```
django-admin.py startproject --template=https://github.com/hapim/django-apiserver/zipball/master <project_name>
```

Getting Started:

```
virtualenv mysiteenv
source mysiteenv/bin/activate
pip install Django==1.7.5
django-admin.py startproject --template=https://github.com/hapim/django-apiserver/zipball/master apiserver
cd apiserver
chmod +x manage.py
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites
./manage.py runserver
```
