from flask_pymongo import MongoClient


CONNECTION_STRING = "mongodb+srv://user1:mb_test12345@cluster0.tmwn7.mongodb.net/mb_test?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
# db = client['mb_test']
# users = db["users"]
# requests = db["requests"]
# posts = db["posts"]

# db = client.mb_test
db = client.user_applications
posts = db.posts
# users = db.users
