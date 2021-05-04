from datetime import datetime

from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.netflix_genres

with open('genres.json', 'r', encoding='utf-8') as file:
    genres = loads(file.read())
    for index, genre in enumerate(genres):
        print(index)
        genre['_created_at'] = datetime.now()
        db.genres.insert(genre)
