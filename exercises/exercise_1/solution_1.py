#-*- coding: utf-8 -*-
u'''
Solution exercise 1: old-style vs. new-style, classes customization
'''


from optparse import OptionParser
from collections import OrderedDict


class CustomOptionParser(OptionParser, object):
    def __str__(self):
        return self.__class__.__name__


class CustomOrderedDict(OrderedDict):
    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self.items()[key])
        return OrderedDict.__getitem__(self, key)

    def __add__(self, other):
        res = self.__class__(self)
        res.update(other)
        return res

    def __sub__(self, other):
        res = self.__class__(self)
        [res.pop(k, None) for k in other]
        return res


class AttrDict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        if name in self:
            self[name] = value
        else:
            # self.__dict__[name] = value  # Perform action instead of delegating
            dict.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            # del self.__dict__[name]  # Perform action instead of delegating
            dict.__delattr__(self, name)
