# inventory-Api

To run this app on your local machine you can simply follow the instructions given below.

To install dependencies you can run

`pip install -r requirements.txt`

To create superuser run this command:

`python manage.py createsuperuser`

and then enter your username, email and password.

To make migrations :

`python manage.py migrate`

To run server :

`python manage.py runserver`

After starting server go to your web browser and visit

`http://127.0.0.1:8000/core/lodolist/`

and for admin module visit

`http://localhost:8000/admin`

and login using superuser credentials.
