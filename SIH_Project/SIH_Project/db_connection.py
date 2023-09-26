import pymongo

url = 'mongodb+srv://nitjec22:zof6PSHkiifCzyt4@cluster0.3w273ju.mongodb.net/'

client = pymongo.MongoClient(url)

db = client['data']