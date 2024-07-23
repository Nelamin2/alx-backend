#!/usr/bin/python3
""" LFU caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache class """
    class LFUCache(BaseCaching):
        def __init__(self):
            super().__init__()
            self.frequency = {}
            self.usage = {}
            self.time = 0

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the LFU key to remove
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min(self.frequency.values())]
                if len(lfu_keys) > 1:
                    # If there's a tie, use the LRU key among the LFU keys
                    lru_key = min(lfu_keys, key=lambda k: self.usage[k])
                else:
                    lru_key = lfu_keys[0]
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.usage[lru_key]
            self.cache_data[key] = item
            self.frequency[key] = 1
        # Update usage time
        self.time += 1
        self.usage[key] = self.time

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.time += 1
        self.usage[key] = self.time
        return self.cache_data[key]
