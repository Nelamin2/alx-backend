#!/usr/bin/python3
""" MRU caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache class """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.queue.pop()
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.queue.append(key)
        else:
            pass

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
        return None
