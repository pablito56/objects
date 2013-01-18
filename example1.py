#-*- coding: utf-8 -*-
u'''
EXAMPLE 1: Classes
'''


# Let's create an old-style class
class MyOldClass:
    def print_instance_class(self):
        print type(self)
        print self.__class__

old_inst = MyOldClass()
old_inst.print_instance_class()


# Let's create an identical new-style class
class MyNewClass(object):
    def print_instance_class(self):
        print type(self)
        print self.__class__

new_inst = MyNewClass()
new_inst.print_instance_class()


#===============================================================================
# - New-style classes introduced in 2.2 to unify classes and types
# - Provide unified object model with a full meta-model
# - Other benefits: subclass most built-in types, descriptors (slots, properties, static and class methods)...
# - By default all classes are old-style until Python 3
#
# - Other changes introduced: __new__, new dir() behavior, metaclasses, new MRO (also in 2.3)
#
# - More info: http://www.python.org/doc/newstyle/
#===============================================================================


# Let's customize our classes
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

    def __str__(self):
        return "{0} / {1}".format(self.num, self.den)

    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__, self.num, self.den)

    def value(self):
        return float(self.num) / self.den

    def __lt__(self, other):
        try:
            return self.value() < other.value()
        except AttributeError:
            return self.value() < other

    def __le__(self, other):
        try:
            return self.value() <= other.value()
        except AttributeError:
            return self.value() <= other

    def __eq__(self, other):
        try:
            return self.value() == other.value()
        except AttributeError:
            return self.value() == other

    def __ne__(self, other):
        try:
            return self.value() != other.value()
        except AttributeError:
            return self.value() != other

    def __gt__(self, other):
        try:
            return self.value() > other.value()
        except AttributeError:
            return self.value() > other

    def __ge__(self, other):
        try:
            return self.value() >= other.value()
        except AttributeError:
            return self.value() >= other

    def __getitem__(self, key):
        if key == 0 or key == 'num':
            return self.num
        elif key == 1 or key == 'den':
            return self.den
        else:
            raise KeyError(key)


f1 = MyFraction(4, 2)
f2 = MyFraction(3, 2)


print f1
print repr(f2)


print f1 == 2
print f2 <= f1


print f1['num'], "/", f1[1], "==", f1


class MirrorFloat(float):
    def __new__(cls, val=0):
        inst = float.__new__(cls, 1.0/val)
        inst.val = val
        return inst

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, self.val)

    def __add__(self, other):
        return float.__sub__(self, other)

    def __sub__(self, other):
        return float.__add__(self, other)


inst = MirrorFloat(-7)
print inst
print repr(inst)


print inst + 2
print inst - 1.3
