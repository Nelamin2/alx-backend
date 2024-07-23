#!/usr/bin/python3
""" LFU caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFU cache class """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.cache = OrderedDict()
        self.freq = {}  # To keep track of frequencies
        self.usage = {}  # To keep track of last access time

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.cache:
            # Update the value and frequency
            self.cache[key] = item
            self.freq[key] += 1
            self.usage[key] = len(self.cache)
        else:
            if len(self.cache) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item
                min_freq = min(self.freq.values())
                # Get all keys with the minimum frequency
                min_freq_keys = [k for k,
                                 v in self.freq.items() if v == min_freq]
                # Use LRU among LFU keys
                lru_key = min(min_freq_keys, key=lambda k: self.usage[k])
                # Remove the LFU item
                del self.cache[lru_key]
                del self.freq[lru_key]
                del self.usage[lru_key]
                print(f"DISCARD: {lru_key}")
            # Add the new item
            self.cache[key] = item
            self.freq[key] = 1
            self.usage[key] = len(self.cache)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache:
            return None
        # Update frequency and access time
        self.freq[key] += 1
        self.usage[key] = len(self.cache)
        return self.cache[key]

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.count[key] += 1
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
        return None
