#!/usr/bin/env python3
""" defines a class Cache"""
import redis
import uuid
from typing import Union, Type, Callable, Optional


class Cache():
    """ stores an instance of the redis client"""
    def __init__(self):
        """ Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """" generate a random key using uuid"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ extract informtion saved in redis"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ Automatically parametrize Cache.get
            with the correct conversion function.
        """
        value = self._redis.get(key)
        return value.decode('UTF-8')

    def get_int(self, key: str) -> int:
        value = self._redis.get(key)
        try:
            value = int(value.decode('UTF-8'))
        except Exception:
            value = 0
        return value
