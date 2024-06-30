#!/usr/bin/python3
""" 100-lfu_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache (BaseCaching):
    """
    LFUCache: class that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """
        LFUCache constructor
        """
        super().__init__()
        self.queue = []  # FIFO queue
        self.map = {}  # LFU map

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        data = self.cache_data
        queue = self.queue
        map = self.map

        if key in data:
            # Move the key to the end to mark it as the most recently used
            queue.remove(key)
            queue.append(key)
            map[key] += 1
        else:
            # If the cache is full, remove the least frequent item
            if len(data) == self.MAX_ITEMS:
                least_freq_items = list(map.keys())
                least_freq_items.sort(key=lambda k: (map[k], queue.index(k)))
                least_freq_item = least_freq_items[0]

                del data[least_freq_item]
                del map[least_freq_item]

                queue.remove(least_freq_item)
                print("DISCARD:", least_freq_item)

            queue.append(key)
            map[key] = 1

        # Update the cache data with the new item
        data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        data = self.cache_data
        queue = self.queue
        map = self.map

        if key is None or key not in data:
            return None

        # Move the key to the end to mark it as the most recently used
        queue.remove(key)
        queue.append(key)

        # Increase the key frequecy counter
        map[key] += 1

        return data.get(key)
