from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def create_news(data):
    db.news.insert_many(data)


def insert_or_update(notice):
    return (
        db.news.update_one(
            {"url": notice["url"]}, {"$set": notice}, upsert=True
        ).upserted_id
        is not None
    )


def find_news():
    return list(db.news.find({}, {"_id": False}))


def find_news_by_title(title):
    return list(
        db.news.find(
            {"title": {"$regex": title, "$options": "i"}},
            {"_id": 0, "title": 1, "url": 1},
        )
    )


def aggregate_most_engage():
    return list(
        db.news.aggregate(
            [
                {
                    "$project": {
                        "title": 1,
                        "url": 1,
                        "sum": {"$sum": ["$shares_count", "$comments_count"]},
                    }
                },
                {"$sort": {"sum": -1, "title": 1}},
                {"$limit": 5},
            ]
        )
    )


def search_news(query):
    return list(db.news.find(query))
