from datetime import timedelta
from settings import SECRET_KEY

MONGO_URI = "mongodb://localhost:27017/myDatabase"

SECRET_KEY = SECRET_KEY

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_TIME_LIMIT= None