#!/usr/bin/env python3
"""  provides stats about nginx"""


from pymongo import MongoClient


def get_method_logs(col, method):
    get = col.count_documents({"method" : method})
    return get

def log_stats():
    """provides stats about Nginx logs stored in MongoDB"""
    # Connect databse
    client = MongoClient()
    db = client["logs"]
    col = db["nginx"]

    logs = col.count_documents({})
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    methodCount = col.find({"method" : "GET"})
    stats = 1200

    # Print output
    print(logs, "logs")
    print("Methods:")

    for i in methods:
        logs = get_method_logs(col, i)
        print("\t", "method {}:".format(i), logs)

    print(stats, "status check")

# call main function
log_stats()

