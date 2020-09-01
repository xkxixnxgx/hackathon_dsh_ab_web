from flask_pymongo import MongoClient
from settings import CONNECTION_STRING


client = MongoClient(CONNECTION_STRING)
db = client.user_applications
posts = db.posts

