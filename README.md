E-Commerce Website Built with Django

This is an E-Commerce website built using Django. It features a user-friendly interface for browsing products, adding items to the shopping cart, and completing a purchase. The platform includes user authentication (registration, login, logout), as well as the ability to manage orders and cart items.
Table of Contents

    Features

    Technologies Used

    Installation

    Setup Instructions

    Usage

    Testing

    License

Features

    User Authentication: Allows users to register, log in, and log out of the website.

    Product Browsing: Displays products with details like price and description.

    Add to Cart: Users can add items to the shopping cart for later checkout.

    Checkout Process: Users can proceed with their purchases and receive an order confirmation.

    Admin Panel: An admin interface to manage products, users, and orders.

Technologies Used

    Django: A Python web framework used to build the backend of the website.

    SQLite: Database to store user, product, and order information.

    Bootstrap: For styling the front-end and creating a responsive design.

    HTML/CSS/JavaScript: Front-end technologies for building the website structure, layout, and interactivity.

Installation
Clone the Repository

To get started, clone this repository to your local machine using the following command:

git clone https://github.com/SeverusSnapee/E-COMMERCE-WEBSITE-DJANGO-.git

Install Dependencies

Make sure you have Python 3 installed on your system. You can install the required dependencies using pip by running:

pip install -r requirements.txt

Create Database Migrations

After setting up the project, make sure to migrate the database by running the following command:

python manage.py migrate

Create a Superuser

To access the Django admin panel, you need to create a superuser by running:

python manage.py createsuperuser

You'll be prompted to provide a username, email, and password for the superuser account.
Start the Development Server

Now you can start the Django development server:

python manage.py runserver

By default, the server runs on http://127.0.0.1:8000/.
Setup Instructions

    Clone the repository to your local machine.

    Create a virtual environment (optional but recommended).

    Install dependencies using pip install -r requirements.txt.

    Run python manage.py migrate to set up the database.

    Start the development server using python manage.py runserver.

Usage

    Open http://127.0.0.1:8000/ in your web browser.

    You will see the homepage with a list of products. You can browse the products, add them to your cart, and proceed to checkout.

    For administrative tasks, access the Django admin panel by navigating to http://127.0.0.1:8000/admin/ and logging in with the superuser account you created.

Testing

To run the tests, use the following command:

python manage.py test

This will execute any test cases written in the tests.py file.
