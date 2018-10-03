class Config:

    DEBUG = False

class DevelopmentConfig(Config):

    DEBUG = True
    TESTNG = True
    DATABASE_URL = "dbname=FastFoodFast_test user=postgres password=password host=localhost"

class TestConfig(Config):

    DEBUG = False
    TESTING = True
    DATABASE_URL = "dbname=FastFoodFast_test user=postgres password=password host=localhost"



