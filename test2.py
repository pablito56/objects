#-*- coding: utf-8 -*-
u'''
Created on Jan 17, 2013

TEST1: Test classes declaration with empty lines

@author: pev
'''


class MyPrintClass(object):
    class_attr = "class_attr_value"

    def __init__(self):
        self.attr = "inst_attr_value"
        self.print_count = 0

    def __str__(self):
        return " | ".join((self.class_attr, self.attr, str(self.print_count)))

    def __repr__(self):
        return "MyPrintClass({0})".format(str(self))

    def print_inst(self):
        self.print_count += 1
        print self
        print repr(self)



inst = MyPrintClass()
print inst
inst.print_inst()
