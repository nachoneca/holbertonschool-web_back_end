#!/usr/bin/env python3
"""Update topics in a Mongo collection"""


def update_topics(mongo_collection, name, topics):
    """Update topics in a Mongo collection"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
