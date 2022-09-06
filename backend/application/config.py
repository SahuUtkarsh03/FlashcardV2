import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = None
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    CELERY_BROKER_URL="redis://localhost:6379/1"
    CELERY_RESULT_BACKEND="redis://localhost:6379/2"
    REDIS_URL = "redis://localhost:6379"
    
class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLITE_DB_DIR = os.path.join(basedir,"../db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+ os.path.join(SQLITE_DB_DIR,"test_db.sqlite3")
    SECRET_KEY= "whatever_is_the_secret_key"
    WTF_CSRF_ENABLED = False
    REDIS_URL = "redis://localhost:6379"
    CELERY_BROKER_URL="redis://localhost:6379/1"
    CELERY_RESULT_BACKEND="redis://localhost:6379/2"
    CACHE_TYPE= "RedisCache"  
    CACHE_REDIS_HOST="localhost"
    CACHE_REDIS_PORT=6379
    CACHE_DEFAULT_TIMEOUT= 300 
    
class ProductionConfig(Config):
    DEBUG = False
    SQLITE_DB_DIR = os.path.join(basedir,"../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+ os.path.join(SQLITE_DB_DIR,"production_db.sqlite3") or "Whatever is your productionDB URI"