# Freelance Solution

Project Milestone Four - Code Institute

https://freelance-solution.herokuapp.com/

The Freelance Solution app was developed and deployed by Alen Krga as the last project for the Code Institute Software Development diploma.
This website is to emulate a freelancing website that provides already existing freelance designs or a custom design as requested by the user.

## Table of contents

1. [UX](#UX)
    1. [Design process](#Design-process)
    2. [Design choices](#Design-choices)
    3. [Fonts](#Colors)
    4. [Wireframes](#Wireframes)
2. [Features](#Features)
    1. [Accounts](#Accounts)
        1. [Register page](#Register-page)
        2. [Login page](#Login-page)
        3. [Profile page](#Profile-page)
        4. [Reset password](#Reset-password)
        5. [Logout](#Logout)
    2. [Home page](#Home-page)
    3. [Products page](#Products-page)
        1. [Product details](#Product-details)
    4. [Request a design](#Request-a-design)
    5. [Cart](#Cart)
    6. [Checkout](#Checkout)
    7. [Admin panel](#Admin-panel)
    8. [404 page](#404-page)
    9. [Features left to implement](#Features-left-to-implement)
3. [Technologies](#Technologies)
    1. [Tools](#Tools)
    2. [Libraries and frameworks](#Libraries-and-frameworks)
    3. [Languages](#Languages)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
    1. [Instructions](#Instructions)
    2. [Deployment to Heroku](#Deployment-to-Heroku)
6. [Credits](#Credits)
    1. [Media](#Media)
    2. [Code](#Code)

# UX

## Design process
The main goal of the website was to show-off the admin's designs and make them easily available for purchase. So the whole design process was based around that goal. The home page is simple yet informative and has multiple links to the Products page and the Custom Design page. To increase the maximum reach of the website, all users can view all the products, not only authenticated ones. For more advanced features the authentication is required. User's info is used as much as possible to avoid the user having to type in his info more than once on the website.
The point is to get the user to make a purchase in the least ammount of steps. This led to the current design: a simple yet informative home page with quick access to all the selling parts of the website. The user can quickly search for an item and add it to the cart, so the checkout had to be quick as well. Thanks to Django and Stripe it was more than possible to achieve that.
The admin offers a few different options, so I had to include types in the Product model. That made the 'Filter' option a must-have in the app to make it even faster for users to find what they need.
Lastly, for those who want a bit more than the products offer, there is an easy-to-access page for submitting a custom design request. This was a complete must from the beggining of the project, to maximize the sales. To further decrease the number of steps to complete a request for a design, the built-in calculator shows the price immediately and the user can checkout using the Stripe's payment form.

## Design choices
This website was designed to get the user a design that suits their needs as fast as possible. It has a database of production-ready designs but also gives the clients the opportunity to request a custom-tailored design.

Every screen contains a NavBar and a Footer. The Navbar, depending if the user is authenticated, shows different buttons. Anonymous users can log in and register, while authenticated users can view their profile and log out.
Footer has a 'Contact me' link that opens up a Contact Me form.

Every screen has a 'Scroll to Top' feature, a button showing up at the right-bottom part of the screen, when the user scrolls. Pressing the button brings the user to the top of the page.

### Fonts
- The font used in this project is [Lato](https://fonts.google.com/specimen/Lato#about) which is an user friendly mainly used by its creator Google to give a proper reading in different screen sizes.

### Wireframes
The wireframes developed for this project was only taken three types of devices, desktop, tablet and mobile.
In addition, the tool used to develop this wireframes was [Balsamiq](https://balsamiq.com/) giving the ability to a rapid design.
  - [Mobile devices](https://freelance-solution.herokuapp.com/static/wireframes/Mobile.png)
  - [Desktop devices](https://freelance-solution.herokuapp.com/static/wireframes/Desktop.png)

# Features

Freelance Solution website is composed by five different applications: `accounts`, `cart`, `checkout`, `products`, `home` and `orders`. Using MVC architecture from the Django framework, each application is a separate stand-alone module that can be reused in other applications.

## Accounts
Users have the ability to create their account, log in and reset their password if needed.    

### Register page
  - A username, email and password are required to create an account.
  - Username must be unique.
  - Password must contain at least 8 characters.

### Login page
  - A username (or email) and password of an already existing account are required to sign in.

### Profile page
  - Authenticated users only. Provides a view of purchased products and pending orders by the user. The user can download high resolution files of the products they bought.

### Contact me
  - Anyone can type in their email and a message they want to send to the admin. After submitting the form, the admin gets an email with all the info, and the user also gets an email confirming that they sent the email.

### Reset password
  - Step 1: at the login page, you can find the `forgot my password` link in which will lead to a form to enter your account email.
  - Step 2: Add the email from the account you need to reset the password.
  - Step 3: You will receive an email with a link that opens a new window that allows you to set a different password for your account.
  - Step 4: Once the password is set you can login with the new password.

### Logout
  - Logs out the currently authenticated user and clears the session (removes everything from the cart).

## Home page
Home page introduces the user to Alen Krga and his work. It also holds all the neccessary navigation for the user and makes it easier for the user to navigate to the most important pages for him: Products and Request a design. Most of the users will find what they need on the Products page but for those needing a bit more customized designs or something completely unique, they can submit a request for a custom design.

## Products page
Initially shows all products. The user can then type in a search parameter and choose a category to filter by. Pressing the button 'Filter' the page loads with the search results. The user can view a title, description and price, and quickly add an item to the cart. Clicking on a product opens a 'Product details' page.

### Product details
Shows all the product details, including full-length description. The user has an additional option of choosing a quantity before adding to cart. Quantity represents an ammount of different variations of the product the user gets.
Below is the 'Reviews' section, where you can read reviews of users that bought the product. Only users who have the product can write a review.

## Request a design
Users who need a more customized design can request a custom design through this form. Description and design type are required. A Javascript-built calculator then calculates the price for the user and the user pays immediately. The price is of course calculated on the backend again, for security reasons. The user then gets an email confirmation of the requested order, and the admin gets an email informing him of the new order.

## Cart
 The cart gives the user the ability to view and edit the cart as they wish. The user can view products in the cart, edit the quantity or delete the product altogether. After that the user proceeds to the 'Checkout' page by clicking the button 'Checkout'.

## Checkout
  - The checkout application holds and manipulates the `Stripe` API. In which empowers the overall application with the e-commerce functionality.
  - In this application is developed and performed the forms users who are willing to buy any retreat, to plot their details into the checkout application forms and finalise the purchase.

## Admin panel
The admin panel has 4 custom registered apps: Accounts, Orders and Products. In these apps there are 5 different models registered (ContactMe, Orders, ProductReviews, Products and UserProducts). The admin can perform CRUD operations on all of them. Only admin users have access to the Admin panel.

## 404 page

  - Custom styled 404 page, giving the user the ability to navigate back.


## Features Left To Implement
   1. Admin page graphs to display data from comments, sales and views.
   2. Automatic generation of thumbnails for products.
   3. More product types.
   4. Multiple images for a product.
   5. Order Status inside Profile page.

# Technologies

## Tools

  - [Stripe](https://stripe.com/ie) to receive payments.
  - [Heroku](https://www.heroku.com/) for hosting the application and deploy.
  - [AWS S3](https://aws.amazon.com/s3/) was used as a cloud service to host static files.
  - [Github](https://github.com/) to share and store code remotely.
  - [Git](https://git-scm.com/) was used to manage version control.
  - [Sqlite3](https://www.sqlite.org/index.html) a database provided by django for development.
  - [PostgreSQL](https://www.postgresql.org/), a robust database provided by Heroku for production development.
  - [Balsamiq](https://balsamiq.com/) for the wireframes design.

## Libraries and frameworks

  - [Django](https://www.djangoproject.com/) a high level python web-framework used to design this project.
  - [Bootstrap 4](https://getbootstrap.com/) a CSS library grid used for the development of this site.
  - [Ionicons](https://ionicons.com/) for the creation and implementation of icons.
  - [Google fonts](https://fonts.google.com/) to bring custom font styling.
  - [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/#description) used as the Python PostgreSQL adapter.
  - [Jquery](https://jquery.com/) a Javascript library to simplify the code.
  - [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) a library that enables python code to modify AWS service.

## Languages

  - This project uses HTML, CSS, Javascript and Python programming languages.


# Testing

Sadly except manual testing, I didn't have enough time to write unit tests.
   - There are no dead links on the website.
   - There are no errors and warnings in the Developer console
   - The page is fully responsive and has been tested using the Developer console.

## Mobile
  - Galaxy S5
  - Pixel 2
  - Pixel 2 XL
  - iPhone 4
  - iPhone 5 SE
  - iPhone 6, 7 and 8
  - iPhone 6, 7 and 8 Plus (real device)
  - iPhone X

## Tablet
  - iPad
  - iPad Pro

## Laptop
  - Macbook

## Browsers
  - Chome
  - Safari
  - Firefox
  - Opera

## Bugs
  - There are no known bugs. If you find a bug, please report it!


# Deployment

For the deployment you will need tool as:

  - An IDE such as [Atom](https://atom.io/) or [Visual Studio Code](https://code.visualstudio.com/).
  - Have installed in your machine [Python 3](https://www.python.org/downloads/) and [Git](https://git-scm.com/).

To continue on the process of deployment you should have accounts on the following services:

  - [Stripe](https://stripe.com/ie)
  - [AWS](https://aws.amazon.com/s3/)
  - [Gmail](https://gmail.com)

### Instructions
  1. Download a copy of this repository from the link https://github.com/AlenKrga1/FreelanceSolution.git as a download zip file. Or at your terminal do the following git command:

      ```
      $ git clone https://github.com/AlenKrga1/FreelanceSolution.git
      ```
  2. If you downloaded the project as a zip file, unzip it and add it in your directory.
  3. To not run in some unexpected behaviours during development, a virtual environment is advised to be used before the project be installed in your machine. So create a virtual environment with the command:

      ```
     $ python -m venv venv
      ```
  4. After you already created the virtual environment folder you need to activate it:

      ```
      $ source venv/bin/activate
      ```
  5. Install requirements.txt file.

      ```
      $ pip install -r requirements.txt
      ```
  6. Create a `local_settings.py` file inside `freelancesolution` to store development variables:
     ```
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = <secret key>

    DEBUG = True

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    EMAIL_HOST_USER = <your gmail username>
    EMAIL_HOST_PASSWORD = <your gmail password>

    STRIPE_PUBLISHABLE = <Stripe publishable key>
    STRIPE_SECRET = <Stripe secret>
     ```

  7. Migrate the models to crete a database template.

      ```
      $ python manage.py migrate
      ```
  8. In this step you will need to create a super user to have access to the admin page.

      ```
      $ python manage.py createsuperuser
      ```
  9. So, after you do all the steps to create a super user you can now run the server.

      ```
      $ python manage.py runserver
      ```
  10. After the server is running locally add the `/admin` path at the end of the url link. It might look like this if you are not running another application.

      ```
      http://127.0.0.1:8000/admin
      ```

### Deployment to Heroku

To make the deployment of this application to `Heroku` you will need to do the following steps.

  1. Signup for [Heroku](https://signup.heroku.com/)
  2. Install [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli)
  3. After installing `Heroku toolbelt` add the following code into your termial and login into your account you already create.
     ```
     $ heroku login
      Enter your Heroku credentials.
      Email: your@email.com
      Password (typing will be hidden):
      Authentication successful.
     ```
  4. Save all the requirements into the `requirements.txt` as mentioned before with the command:
     ```
     $ pip freeze > requirements.txt
     ```
  5. Create a file named `Procfile` and add the following config.
     ```
     release: python manage.py migrate
     web: gunicorn freelancesolution.wsgi:application
     ```
 6. After all the setup is done `git add .`, `git commit` and `git push` your application to a repository you created on Github.
 7. In your `Heroku`account click new and create new app.
 9. Select your region and create a name for your project.
10. In your `Heroku` settings click `reveal config vars`.
11. Add the following config variables:

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| AWS_STORAGE_BUCKET_NAME | `<your postgres database url>`  |
| DATABASE_URL | `<your postgres database url>`  |
| EMAIL_ADDRESS | `<your email address>`  |
| EMAIL_PASSWORD | `<your email password>` |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLISHABLE | `<your stripe publishable key>`  |
| STRIPE_SECRET | `<your stripe secret key>`  |
| USE_S3 | `TRUE`  |

12. Add a development (postgres) database:
  ```
  $ heroku addons:add heroku-postgresql:dev
    heroku addons:add heroku-postgresql:dev
    Adding heroku-postgresql on deploy_django... done, v13 (free)
    Attached as HEROKU_POSTGRESQL_COPPER_URL
    Database has been created and is available
    ! This database is empty. If upgrading, you can transfer
    ! data from another database with pgbackups:restore.
    Use `heroku addons:docs heroku-postgresql` to view documentation.

  $ heroku pg:promote HEROKU_POSTGRESQL_COPPER_URL
    Promoting HEROKU_POSTGRESQL_COPPER_URL to DATABASE_URL... done
   ```
13. After adding the config into your dashboard add the following commands.
  - `$ heroku login`
  - `heroku git:remote -a test-app-to-deploy`
  - `$ git push heroku master`

14. On your `Heroku` dashboard click on `open app` button and check if the application is running correctly.

# Credits

## Media
  - The photos used in the project were downloaded from [Logoipsum](https://logoipsum.com/), platform that provides copyright-free placeholders.

## Code
  - The `accounts`, `cart` and `checkout` apps were recycled from the [Code Institute](https://github.com/Code-Institute-Org) lessons but modified to fit with the project purpose.