#!usr/bin/env python3
""" defines a class Cache"""
import redis
import uuid


class Cache():
    """ stores an instance of the redis client"""
    def __init__(self):
        """ instatiate the Cache object"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: any) -> str:
        """" generate a random key using uuid"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key