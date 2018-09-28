# Fast-Food-Fast
Fast-Food-Fast is a delivery service for a restaurant.

You can acess it at:
    https://kicaronaldokello.github.io/Fast-Food-Fast/UI/
    
   [![Build Status](https://travis-ci.org/KicaRonaldOkello/Fast-Food-Fast.svg?branch=api)](https://travis-ci.org/KicaRonaldOkello/Fast-Food-Fast)
   [![Maintainability](https://api.codeclimate.com/v1/badges/153f76beb7e25267ced5/maintainability)](https://codeclimate.com/github/KicaRonaldOkello/Fast-Food-Fast/maintainability)
   [![Coverage Status](https://coveralls.io/repos/github/KicaRonaldOkello/Fast-Food-Fast/badge.svg?branch=api)](https://coveralls.io/github/KicaRonaldOkello/Fast-Food-Fast?branch=api)
   
  Heroku link:
    https://fast-food-fas.herokuapp.com/api/v1/orders
   
   
# Getting Started.
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
# Prerequisites.
- Serverside Framework: Flask Python Framework.
- Testing Framework: PyTest
- API development environment: Postman


# Installing.
- Create a directory called Fast-Food-Fast.

    `mkdir Fast-Food-Fast`
- Enter the directory.

    `cd Fast-Food-Fast`
- Clone the project from github using:

     git clone http://www.github.com/KicaRonaldOkello/Fast-Food-Fast/tree/api
- Install virtualenvironment.

    `pip install virtualenv`
- Activate virtualenvironment 

    `. bin/activate`
- Install flask

    `pip install flask`
- Install Postman.
 # Running the API.
 - Run the flask app in your terminal.
 
    `python run.py`
    
 -There are 4 endpoints which can be accessed in the following way.
 
   | Method | Endpoint | Status Code |
   |--------|----------|-------------|
   | GET | "/api/v1/orders" | 200 |
   | GET | "/api/v1/orders/\<orderId>\" | 200 |
   | POST | "/api/v1/orders" | 201 |
   | PUT | "/api/v1/orders/\<orderId>\" |201 |
    
  
 - Open Postman, choose any of the methods from the table and enter its approopiate end point.
 - After clicking send, Postman should return the corresponding status code.
  
 # Features.
 - users can post orders.
 - Users can get all orders.
 - Users can get one order.
 - Users can update order status.
  
  # Running unittests.
  In order to know whether our endpoints are working, we can run unittests.
  - In your terminal:
  
    `pip install pytest`
  - Test your endpoints in the terminal
  
    `pytest tests/test_views.py`
  - It returns results showing which endpoints passed the tests and which endpoints failed the tests.
  
  # Authors.
  - Kica Ronald Okello.
