"""
Module providing a hostname resolver with caching abilities
"""

import socket

"""
Class that caches calls to socket.gethostbyname(host)

Instantiate via:
from resolver import Resolver
resolve = Resolver()
resolve('sixty-north.com')
"""
class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()
    
    def has_host(self, host):
        return host in self._cache
