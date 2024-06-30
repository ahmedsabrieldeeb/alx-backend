#!/usr/bin/python3
""" 1-fifo_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache (BaseCaching):
    """
    LRUCache: class that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """
        LRUCache constructor
        """
        super().__init__()
        self.queue = []  # FIFO queue

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        data = self.cache_data
        queue = self.queue

        if key in data:
            # Move the key to the end to mark it as the most recently used
            queue.remove(key)
            queue.append(key)
        else:
            # If the cache is full, remove the oldest item
            if len(data) == self.MAX_ITEMS:
                oldest_key = queue.pop(0)
                del data[oldest_key]
                print(f"DISCARD: {oldest_key}")

            queue.append(key)

        # Update the cache data with the new item
        data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        data = self.cache_data
        queue = self.queue

        if key is None or key not in data:
            return None

        # Move the key to the end to mark it as the most recently used
        queue.remove(key)
        queue.append(key)

        return data.get(key)
