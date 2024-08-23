#!/usr/bin/env python3
"""Return a list of the docs in de DB with the matched topics"""


def schools_by_topic(mongo_collection, topic):
    """Return a list of the docs in de DB with the matched topics"""
    return [doc for doc in mongo_collection.find() if (topics := doc.get('topics')) and topic in topics]
