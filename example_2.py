#-*- coding: utf-8 -*-
u'''
EXAMPLE 2: super, getattr and MRO
'''

# Let's implement a verbose dict
class VerboseDict(dict):
    def __getitem__(self, key):
        print "__getitem__", key
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        print "__setitem__", key, value
        return dict.__setitem__(self, key, value)

    def __getattr__(self, name):
        print "__getattr__", name
        return dict.__getattr__(self, name)

    def __setattr__(self, name, value):
        print "__setattr__", name, value
        return dict.__setattr__(self, name, value)


# Let's use this dict
vd = VerboseDict({'a': 1, 'b': 2})
vd['c'] = 3
vd['c']
vd.x
vd.x = 7


#===============================================================================
# What if we want to mix this behavior wuth out AttrDict?
#===============================================================================

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
            self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            del self.__dict__[name]

# Option 1: inherit from both
class VerboseAttribDict(VerboseDict, AttrDict):
    pass

# Let's use this dict
vd = VerboseAttribDict({'a': 1, 'b': 2})
vd['c'] = 3
vd['c']
vd.x
vd.x = 7


# Option 2: inherit from both (change the order)
class VerboseAttribDict(AttrDict, VerboseDict):
    pass

# Let's use this dict
vd = VerboseAttribDict({'a': 1, 'b': 2})
vd['c'] = 3
vd['c']
vd.x
vd.x = 7

# Option 3: reimplement adding verbose and attrib behavior in single class :-S


#===============================================================================
# The solution is super and cooperative methods!!
# - super(type[, object-or-type])
# - Return a proxy object that delegates method calls to a parent or sibling class of type 
#===============================================================================

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

# Let's check its MRO
print D.__mro__

#===============================================================================
# In D's m, super(D, self).m() will find and call B.m(self), since B is the first base class following D in D.__mro__ that defines m.
# Now in B.m, super(B, self).m() is called. Since self is a D instance, the MRO is (D, B, C, A, object) and the class following B is C.
# This is where the search for a definition of m continues. This finds C.m, which is called, and in turn calls super(C, self).m().
# Still using the same MRO, we see that the class following C is A, and thus A.m is called. This is the original definition of m, so no super call is made at this point.
#===============================================================================

#===============================================================================
# MRO was changed because in new-style all classes inherit from 'object, so suddenly diamond diagrams could easily appear:
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
