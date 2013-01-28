#-*- coding: utf-8 -*-
u'''
EXAMPLE 2: MRO, super and getattr
'''


class A(object):
    def method(self):
        print type(self), "A's method"


class B(A):
    def method(self):
        print type(self), "B's method"
        super(B, self).method()


class C(A):
    def method(self):
        print type(self), "C's method"
        super(C, self).method()


class D(B, C):
    def method(self):
        print type(self), "D's method"
        super(D, self).method()

#==============================================================================
# We have a diamond inheritance schema:
#
#    A
#   / \
#  B   C
#   \ /
#    D
#==============================================================================


# Let's instantiate D and call the method
d_inst = D()
d_inst.method()

print D.__mro__

#===============================================================================
# In D's m, super(D, self).m() will find and call B.m(self), since B is the first base class following D in D.__mro__ that defines m.
# Now in B.m, super(B, self).m() is called. Since self is a D instance, the MRO is (D, B, C, A, object) and the class following B is C.
# This is where the search for a definition of m continues. This finds C.m, which is called, and in turn calls super(C, self).m().
# Still using the same MRO, we see that the class following C is A, and thus A.m is called. This is the original definition of m, so no super call is made at this point.
#===============================================================================

#===============================================================================
# MRO was changed because in new-style all classes inherit from 'object', so suddenly diamond diagrams could easily appear:
# - Old:
#
#  B   C
#   \ /
#    D
#
#
# - New:
#
#  object
#   / \
#  B   C
#   \ /
#    D
#===============================================================================
