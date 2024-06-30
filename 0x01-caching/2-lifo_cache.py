#!/usr/bin/python3
""" 1-fifo_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache (BaseCaching):
    """
    LIFOCache: class that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """
        BaseCaching constructor
        """
        super().__init__()
        self.stack = []  # LIFO Stack

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        data = self.cache_data
        stack = self.stack

        if len(data) == self.MAX_ITEMS and key not in data:
            last_key = stack.pop()  # Remove the last inserted key
            del data[last_key]
            print("DISCARD: {}".format(last_key))

        if key in data:
            stack.remove(key)  # Remove key if it already exists

        data[key] = item
        stack.append(key)  # Add key to the stack

    def get(self, key):
        """
        Get an item by key
        """
        data = self.cache_data
        if key is None or key not in data:
            return None

        return data.get(key)
