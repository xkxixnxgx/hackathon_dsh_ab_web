from datetime import timedelta


MONGO_URI = "mongodb://localhost:27017/myDatabase"

SECRET_KEY = 'ehuiwevwevwbveu'

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_TIME_LIMIT= None