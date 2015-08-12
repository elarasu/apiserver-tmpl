# django-apiserver

Very opinionated api server. Comes with the following features 
   * authentication (oauth2)
   * user profile

Usage:

```django-admin.py startproject --template=https://github.com/hapim/django-apiserver/zipball/master <project_name>```

Getting Started:

```
virtualenv env
source env/bin/activate
pip install Django==1.8.3
django-admin.py startproject --template=https://github.com/hapim/django-apiserver/zipball/master apiserver
cd apiserver
chmod +x manage.py
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```
