__author__ = 'gengjie'
import pymongo
from pymongo.mongo_client import MongoClient

connection = pymongo.Connection('localhost', 27017)
print connection.database_names()
db = connection.test_database
conllection = db.test_collection

posts = db.posts

# for i in xrange(10000):
#     post = {"author": "Mike"+str(i),
#             "text": "My first blog post!",
#             "tags": ["book", "computer", "TV"],
#             "data": datetime.datetime.now()}
#     posts.insert(post)

print db.collections
print db.collection_names()
print posts.count()
print posts.aggregate({'$group': {'_id': '$text', 'count': {'$sum': 1}}})
for post in posts.find().limit(100):
    print post
posts.remove({'author': 'Mike2'})