from pymongo import MongoClient
import crypto
from botWhileTrue.settings import CONNECTION_STRING

# Mongo
db_link = CONNECTION_STRING
client = MongoClient(db_link)

# База данных
db = client.user_applications

posts = db.posts

def write_data(data: dict):
    encrypted_data = crypto.encrypt_dict(data)
    return posts.insert_one(encrypted_data).inserted_id


def get_data(chat_id) -> list:
    encrypted_data = list(posts.find({'chat_id': chat_id}))
    decrypted_data = []
    for i in encrypted_data:
        data = crypto.decrypt_dict(i)
        decrypted_data.append(data)
    return decrypted_data
