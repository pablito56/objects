#-*- coding: utf-8 -*-
u'''
Exercise 1: old-style vs. new-style, classes customization
'''


from optparse import OptionParser
from collections import OrderedDict


class CustomOptionParser(OptionParser, object):
    def __str__(self):
        return self.__class__.__name__


class CustomOrderedDict(OrderedDict):
    def _pair_str(self, i):
        res = [None, None]
        if isinstance(i[0], str):
            res[0] = "'" + i[0] + "'"
        else:
            res[0] = str(i[0])
        if isinstance(i[1], str):
            res[1] = "'" + i[1] + "'"
        else:
            res[1] = str(i[1])
        return res

    def __str__(self):
        txt = ", ".join(map(": ".join, map(self._pair_str, self.items())))
        return"{" +  txt + "}"

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
