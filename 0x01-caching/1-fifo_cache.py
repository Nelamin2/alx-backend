#!/usr/bin/python3
""" FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.queue:
                    removed = self.queue.pop(0)
                    del self.cache_data[removed]
                    print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
