__author__ = 'gengjie'
import pymongo

connection = pymongo.Connection('localhost', 27017)
db = connection.test_database
conllection = db.test_collection

posts = db.posts

# for i in xrange(10000):
#     post = {"author": "Mike"+str(i),
#             "text": "My first blog post!",
#             "tags": ["book", "computer", "TV"],
#             "data": datetime.datetime.now()}
#     posts.insert(post)

print db.collection_names()
print posts.count()
for post in posts.find().limit(100):
    print post
posts.remove({'author': 'Mike2'})