#-*- coding: utf-8 -*-
u'''
Created on Jan 17, 2013

TEST1: Test classes declaration with empty lines

@author: pev
'''


class MyClass(object):
    class_attr = "class_attr_value"

    def __init__(self):
        self.attr = "inst_attr_value"

    def __str__(self):
        return " | ".join((self.class_attr, self.attr))



inst = MyClass()
print inst
