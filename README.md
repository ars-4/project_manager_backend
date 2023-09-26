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
```
python -m pip install -r requirements.txt
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
```
python manage.py runserver
```
`visit` [http://127.0.0.0.1:8000/admin/](http://127.0.0.0.1:8000/admin/)

Create a `Person` object and add newly created superuser to `Admin` group.

<br>

### Start backend django server with daphne
```
daphne CManager.asgi:application
```

<br>

![project_invoices](/screenshots/project_invoice_list.png)


### Features
- <b>Project Management</b>
    - B2B Client Based Hierarchy
    - Real Time Tasks
    - Kanban Board
    - Project Invoice And Billing
- <b>Employee Management</b>
    - Attendance Management
    - Salary Invoices
    - Tasks And Tickets
- <b>Chat Support</b>
    - Project Wide Chat
    - Client Chat
    - Direct Chat

<br>

### More Information
For [More Information](https://djangoproject.com/).

<br>

<hr>

My website: [ARS](https://dev-ars.vercel.app/)

