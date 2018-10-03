class Config:

    DEBUG = False

class DevelopmentConfig(Config):

    DEBUG = True
    TESTNG = True
    DATABASE_URL = 'postgres://postgres:password@localhost:5432/FastFoodFast'

class TestConfig(Config):

    DEBUG = False
    TESTING = True
    DATABASE_URL = 'postgres://postgres:password@localhost:5432/FastFoodFast_test'