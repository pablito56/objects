#-*- coding: utf-8 -*-
u'''
Exercise 1: old-style vs. new-style, classes customization
'''


from optparse import OptionParser
from collections import OrderedDict


class CustomOptionParser(OptionParser):
    def __str__(self):
        return self.__class__.__name__


class CustomOrderedDict(OrderedDict):

    def __str__(self):
        return OrderedDict.__str__(self)

    def __getitem__(self, key):
        return OrderedDict.__getitem__(self, key)
