class Config:

    DEBUG = False

class DevelopmentConfig(Config):

    DEBUG = True
    TESTNG = True
    DATABASE_URL = 'postgresql://postgres:password@localhost/fast_food_fast'

class TestConfig(Config):

    DEBUG = False
    TESTING = True
    DATABASE_URL = 'postgresql://postgres:password@localhost/FastFoodFast_test'



 