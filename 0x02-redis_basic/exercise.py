#!/usr/bin/env python3
""" defines a class Cache"""
import redis
import uuid
from typing import Union, Type


class Cache():
    """ stores an instance of the redis client"""
    def __init__(self) -> None:
        """ Constructor"""
        self._redis: Type = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """" generate a random key using uuid"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
