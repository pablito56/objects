#-*- coding: utf-8 -*-
u'''
EXAMPLE 1: MRO, super and getattr
'''


class A(object):
    def m(self): print type(self), "save A's data"

class B(A):
    def m(self): print type(self), "save B's data"; super(B, self).m()

class C(A):
    def m(self): print type(self), "save C's data"; super(C, self).m()

class D(B, C):
    def m(self): print type(self), "save D's data"; super(D, self).m()


d_inst = D()
d_inst.m()
