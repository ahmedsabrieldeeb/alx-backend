#!/usr/bin/python3
""" 1-fifo_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache (BaseCaching):
    """
    FIFOCache: class that inherits from BaseCaching
    and is a caching system
    """
    def put(self, key, item):
        """
        Add an item in the cache
        """
        data = self.cache_data
        if key is None or item is None:
            return

        if len(data) == self.MAX_ITEMS:
            data.pop(next(iter(data)))

        data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        data = self.cache_data
        if key is None or key not in data:
            return None

        return data.get(key)
