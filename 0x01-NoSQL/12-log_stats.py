#!/usr/bin/env python3
"""  provides stats about nginx"""

if __name__ == "__main__":
    from pymongo import MongoClient

    def get_method_logs(col, method):
        """ helper function to count logs"""

        return col.count_documents({"method": method})

    def log_stats():
        """provides stats about Nginx logs stored in MongoDB"""
        # Connect databse
        client = MongoClient()
        db = client["logs"]
        col = db["nginx"]

        logs = col.count_documents({})
        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

        # Print output given in example
        print(logs, "logs")
        print("Methods:")

        for i in methods:
            logs = get_method_logs(col, i)
            print("\t", "method {}:".format(i), logs)

        print(col.count_documents(
            {"method": "GET", "path": "/status"}), "status check")


# call main function
    log_stats()
