# Parastar Python Back-End 

This Progrom Demo version in Python Model of Prastar Back-End. 

## Features

 - **[ GET, POST]** methods for Create User
 - **[GET, POST]** methods for Request Service

## Getting Started
To work locally and extend Parastar-Python follow these steps.

 -  Clone the repo from Github

```bash
git clone git@github.com:pooyasoleymani/Parastar-Python.git
```


 #### Requirment install:
 
1. Django Web Framework

```
pip install django==3.1.3
```
2. Django Cors Headers - Used to enable CORS headers in API responses, and allow   requests to be made to your API server from other origins.

```
pip install django-cors-headers==3.5.0
```
3. MySQL Client - Used as an interface to connect Django application to the MySQL server.

```
pip install mysqlclient==2.0.1
```

4. Django REST framework for building Web APIs using Python and Django.

```
pip install djangorestframework==3.12.2
```


## Settings

 ##### Using the URLconf defined in todoapi.urls, Django tried these URL patterns, in this order:
 - admin/
- todos/
- todos/< int : id >/
- serviceRequest/
- serviceRequest/< int : id >/
- servicecatalog/
- servicecatalog/< int : id >/
- api/create-user/ [name='create_user']
- api/create-user/< int : id >/ [name='create_user']
- api/create-token/ [name='create_token']



[Marked]: <https://github.com/markedjs/marked>
[Turndown]: <https://github.com/domchristie/turndown>
[Travis-CI]: <https://travis-ci.com/>

