#!/usr/bin/env python3
"""
task 1
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assign to the dictionary 'self.cache_data'
        the item value for the key 'key'
        """
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                k, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {k}")
            self.cache_data[key] = item
        return

    def get(self, key):
        """
        return the value in 'self.cache_data' linked to 'key'
        """
        return self.cache_data.get(key, None)
