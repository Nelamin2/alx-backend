#!/usr/bin/python3
""" LIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache class """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.stack = []
        
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.stack.pop()
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
