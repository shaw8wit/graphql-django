# graphql-django

A simple GraphQl api to handle coursework in Django.


## Getting Started

+ clone or download the repo and ```cd``` into the ```coursework``` directory.
+ Run ```python manage.py makemigrations``` to make migrations for the app.
+ Run ```python manage.py migrate``` to apply migrations to your database.
+ Add dummy data using ```python manage.py loaddate coursework.json``` to your local db.
+ Run ```python manage.py runserver``` to run the server in your local machine.
+ In the ```urls.py``` set the ```graphiql``` to ```false``` to disable the graphql interface.
+ GraphQl API will be running on the ```graphql/``` endpoint.
+ Basic CRUD on all the models are available, read on how to query a graphql api to learn more.