# Fast-Food-Fast
Fast-Food-Fast is a delivery service for a restaurant.

You can acess it at:
    https://kicaronaldokello.github.io/Fast-Food-Fast/UI/
    
   [![Build Status](https://travis-ci.org/KicaRonaldOkello/Fast-Food-Fast.svg?branch=ft-challenge3)](https://travis-ci.org/KicaRonaldOkello/Fast-Food-Fast)
   <a href="https://codeclimate.com/github/KicaRonaldOkello/Fast-Food-Fast/maintainability"><img src="https://api.codeclimate.com/v1/badges/153f76beb7e25267ced5/maintainability" /></a>
   [![Coverage Status](https://coveralls.io/repos/github/KicaRonaldOkello/Fast-Food-Fast/badge.svg?branch=ft-challenge3)](https://coveralls.io/github/KicaRonaldOkello/Fast-Food-Fast?branch=ft-challenge3)
   
  Heroku link:
 
   
   
# Getting Started.
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
# Prerequisites.
- Serverside Framework: Flask Python Framework.
- Testing Framework: PyTest
- API development environment: Postman
- Python v3+
- PostgreSQL9.2


# Installing.
- If using windows, install python. Go to the link below and choose `python 3.6`, download and install it.

     https://www.python.org/downloads/windows/
     
- Install postgresql. For windows, go to https://www.postgresql.org/download/windows/ and for linux,

      `sudo apt-get update` 
     `sudo apt-get install postgresql postgresql-contrib`
      `sudo -i -u postgres`
      `createdb fast_food_fast`
     
- Create a directory called Fast-Food-Fast.

    `mkdir Fast-Food-Fast`
  
- Enter the directory.

    `cd Fast-Food-Fast`
    
- Clone the project from github using:

     git clone http://www.github.com/KicaRonaldOkello/Fast-Food-Fast/tree/ft-challenge3
     
- Install virtualenvironment.

    `python3 -m venv env`
    
- Activate virtualenvironment 

    `. bin/activate`
    
- Install flask

    `pip install -r requirements.txt`
    
- Install Postman.

 # Running the API.
 - Run the flask app in your terminal.
 
    `python run.py`
    
 -There are 10 endpoints which can be accessed in the following way.
 
   | Method | Endpoint | Status Code |
   |--------|----------|-------------|
   | GET | "/api/v1/orders"                   | 200 |
   | GET | "/api/v1/users/orders/\<orderId>\" | 200 |
   | POST | "/api/v1/users/orders"            | 201 |
   | PUT | "/api/v1/users/orders/\<orderId>\" |201 |
   | GET | "/api/v1/users/orders/\<orderId>\" | 200 |
   | POST| "/api/v1/menu"                     | 201 |
   | GET | "/api/v1/menu"                     | 200 |
   | POST| "/api/v1/auth/admin"                | 200 |
   | POST| "/api/v1/auth/signup"               | 200 |
   | POST| "/api/v1/auth/login"                | 200 |
    
  
 - Open Postman, and enter `localhost:5000/api/v1/auth/admin` and add sign up data. This endpoint signs up an admin.
 - After clicking send, Postman should return the corresponding status code.
 
 - Get the token generated, then use it for `/api/v1/menu` and POST a menu item into the database.
 
 - Sign up users to the database using `/api/v1/auth/signup`
 
 - The tokens got from signing up the users can be used to order for food at `/api/v1/users/orders` using a POST method. If    the token expires, sign in the users to get fresh tokens.
 
 - Users can also return their order history using `/api/v1/users/orders` using a GET method.
 
 - Admin can return a specific order using `api/v1/users/orders/\<orderId>` with a GET method.
 
 - Admin can also alter the status of an order from NEW to COMPLETE, CANCELLED, PROCESSING using `/api/v1/users/orders/<orderId>` with a PUT method.
 
 
  
 # Features.
 - users can post orders.
 - Admin can get all orders.
 - Admin can get one order.
 - Users can signup and signin.
 - Admin can change order status.
 - Admin can add menu
 - A user can get menu
 - A user can return their order history.
 - Admin can signup and signin
  
  # Running unittests.
  In order to know whether our endpoints are working, we can run unittests.
  - In your terminal:
  
    `pip install pytest`
  - Test your endpoints in the terminal
  
    `pytest --cov=app`
  - It returns results showing which endpoints passed the tests and which endpoints failed the tests and it also shows test     coverage.
  
  # Authors.
  - Kica Ronald Okello.
