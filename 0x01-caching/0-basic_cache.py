#!/usr/bin/python3
""" 0-basic_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache (BaseCaching):
    """ Basic Cache """
    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key.
        """
        data = self.cache_data
        if key is None or item is None:
            return

        data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        data = self.cache_data
        if key is None or key not in data.keys():
            return None

        return data[key]
