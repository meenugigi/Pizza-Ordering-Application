# Project 3


To run Application:

open cmd
navigate to project folder (on cmd)
type 'pip install -r requirements.txt'
type 'python manage.py runserver'


This is a web application created using Python and Django.

Note: on running this application using the command 'python manage.py runserver' navigate to "http://127.0.0.1:8000/signup" to begin using the application.

In settings.py, enter your Stripe 'Secret key' and 'Publishable Key'

Requirements implemented in this application:

- Menu: Your web application should support all of the available menu items for Pinnochio’s Pizza & Subs (a popular pizza place in Cambridge). It’s up to you, based on analyzing the menu and the various types of possible ordered items (small vs. large, toppings, additions, etc.) to decide how to construct your models to best represent the information. Add your models to orders/models.py, make the necessary migration files, and apply those migrations.
- Adding Items: Using Django Admin, site administrators (restaurant owners) should be able to add, update, and remove items on the menu. Add all of the items from the Pinnochio’s menu into your database using either the Admin UI or by running Python commands in Django’s shell.
- Registration, Login, Logout: Site users (customers) should be able to register for your web application with a username, password, first name, last name, and email address. Customers should then be able to log in and log out of your website.
Shopping Cart: Once logged in, users should see a representation of the restaurant’s menu, where they can add items (along with toppings or extras, if appropriate) to their virtual “shopping cart.” The contents of the shopping should be saved even if a user closes the window, or logs out and logs back in again.
- Placing an Order: Once there is at least one item in a user’s shopping cart, they should be able to place an order, whereby the user is asked to confirm the items in the shopping cart, and the total (no need to worry about tax!) before placing an order.
Viewing Orders: Site administrators should have access to a page where they can view any orders that have already been placed.
- Personal Touch: Here i have implemented a payment feature using Stripe API.

Walkthrough of the files created:

- Folder name Pizza: is the Django project and folder name Orders: is the app created

- orders/views --> contains all the views for the application

- orders/models --> contains all the models for the application

- orders/forms.py --> contains the signup and login form

- orders/admin.py --> registers the models on the Django Admin site

- orders/urls.py --> conatins the application urls

- orders/templates --> contains html files for signup, login, home page, add and delete orders, view placed orders and to make payments.

- orders/static --> contains static files

- orders/mogrations --> contains the files that are auto generated on running the "python manage.py makemigrations" and then "python manage.py migrate" commands



Application Demo Link: https://youtu.be/CUViq_XIoeo
