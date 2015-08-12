# django-apiserver

Very opinionated api server. Comes with the following features 
   * authentication (oauth2)
   * user profile

## Pre-requisites
   * python 2.7
   * pip/virtualenv

## Usage

```django-admin.py startproject --template=https://github.com/elarasu/apiserver-tmpl/zipball/master <project_name>```

## Instructions

```
virtualenv env
source env/bin/activate
pip install Django==1.8.3
django-admin.py startproject --template=https://github.com/elarasu/apiserver-tmpl/zipball/master apiserver
cd apiserver
chmod +x manage.py
pip install -r requirements.txt
./manage.py migrate
./manage.py syncdb
```

### run
To run the server
``` ./manage.py runserver 0.0.0.0:8080 ```

