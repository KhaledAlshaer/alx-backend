#!/usr/bin/env python3
"""
task 1
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    """

    def put(self, key, item):
        """
        assign to the dictionary 'self.cache_data'
        the item value for the key 'key'
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            k, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {k}")

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in 'self.cache_data' linked to 'key'
        """
        return self.cache_data.get(key, None)
