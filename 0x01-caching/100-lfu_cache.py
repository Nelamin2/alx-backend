#!/usr/bin/python3
""" LFU caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache class """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_count = min(self.count.values())
                while self.queue and self.count[self.queue[0]] == min_count:
                    removed = self.queue.pop(0)
                    del self.cache_data[removed]
                    del self.count[removed]
                    print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.count[key] = 0
            self.queue.append(key)
        else:
            pass

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.count[key] += 1
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
        return None
