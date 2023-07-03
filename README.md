# Project Manager
A simple and easy to use project managment system made using django_rest_framework and vue_js. This repository contains the backend code, frontend code is [here](https://github.com/ars-4/project_manager_frontend.git)

<br>

## Project setup
```
virtualenv venv
```
``` 
venv\Scripts\activate OR source venv/bin/activate 
```
<br>

### Migrate migrations to Database
```
python manage.py migrate
```
<br>

### Create Super User and initial person
```
python manage.py createsuperuser
```
`visit` [http://127.0.0.0.1:8000/admin/](http://127.0.0.0.1:8000/admin/)

Create a `Person` object and add newly created superuser to `Admin` group.

<br>

### Start backend django server
```
python manage.py runserver
```

### More Information
For [More Information](https://djangoproject.com/).

<br>

<hr>

My website: [ARS](https://dev-ars.vercel.app/)

