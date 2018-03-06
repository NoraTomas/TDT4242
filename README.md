# TDT4242
E-commerce project - exercise 2

[![Build Status](https://travis-ci.org/NoraTomas/TDT4242.svg?branch=master)](https://travis-ci.org/NoraTomas/TDT4242)

# How to run the project

To run this project you need to have Django, Python 3.6.x and pip installed.
The recommended IDE is PyCHarm.
Once you have cloned the repo and opened the project in PyCharm, you are
ready to install the needed dependencies.

Make sure pip is available in the terminal, if it is not, you probably need to
add Python Scripts to your path, for example:

C:\Users\YourUserName\AppData\Local\Programs\Python\Python36-32\Scripts

After everything is properly installed you can run the command:

pip install -r requirements.txt to install the dependencies.

We are aware that this process can be a bit cumbersome, so do not hesitate
to contact us if you need help! We can also (if we have not already)
arrange meeting times, so you can run the project from our computers with
the correct setup.


Next, in the command line, run the following commands:
 - "python manage.py makemigrations"
 - "python manage.py migrate"
 - "python manage.py runserver"

 These commands have to be executed in the location where the manage.py-file is
 in the project.

 Afterwards, in your browser, navigate to the following links to
 check that the use cases are finished. To create an admin user please use the
 following command in your terminal:

 - "python manage.py createsuperuser"

 You can also log in to the existing admin-account on
 http://127.0.0.1:8000/admin/:

 username: TestUser
 password: testuser314


 1) http://127.0.0.1:8000/register/ - To register a new user
 1.1) http://127.0.0.1:8000/login - To login a user
 2) http://127.0.0.1:8000/home/ - To see items and add them to the cart,
 also to search items
 3) http://127.0.0.1:8000/admin/ - To log in to the admin panel,
 after logging in, press Items -> Add item, to add new items
 and potential package deals  






