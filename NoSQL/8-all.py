#!/usr/bin/env python3
"""List all in a MongoDB"""


def list_all(mongo_collection):
    """List all in a MongoDB"""
    doc = []
    for _ in mongo_collection.find():
        doc.append(_)
    return doc
