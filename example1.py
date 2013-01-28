#-*- coding: utf-8 -*-
u'''
EXAMPLE 1: Classes: new-style vs. old-style, data model & customization
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
# - New-style classes introduced in Python 2.2 to unify classes and types
# - Provide unified object model with a full meta-model
# - Other benefits: subclass most built-in types, descriptors (slots, properties, static and class methods)...
# - By default all classes are old-style until Python 3
#    - In Python 2 you have to inherit from 'object' to use new-style
#    - You should avoid old-style
#
# - Other changes introduced Python 2.2: __new__, new dir() behavior, metaclasses, new MRO (also in 2.3)
#
# - More info: http://www.python.org/doc/newstyle/
#===============================================================================


# Let's inherit from an old-style class
class MyNewOldClass(MyOldClass):
    pass

new_old_inst = MyNewOldClass()
new_old_inst.print_instance_class()

# Let's inherit from an old-style class
class MyGoodNewOldClass(MyOldClass, object):
    pass

good_new_old_inst = MyGoodNewOldClass()
good_new_old_inst.print_instance_class()


#===============================================================================
# - You can inherit from both old-style classes and 'object' to have new-style classes
#===============================================================================


# Let's create a fractions class
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

    def value(self):
        return float(self.num) / self.den

# Let's instantiate a fraction
fract1 = MyFraction(5, 2)
print fract1
print repr(fract1)


# Let's customize our class representation
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

    def value(self):
        return float(self.num) / self.den

    def __str__(self):
        return "{0} / {1}".format(self.num, self.den)

    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__, self.num, self.den)

# Let's instantiate again
fract1 = MyFraction(5, 2)
print fract1
print repr(fract1)


#===============================================================================
# - There are special method names to customize your classes behavior
# - Python invokes these methods (if present) when special syntax is executed
#    - Instatiation and object creation
#    - Representation
#    - Rich comparison
#    - Arithmetic operations
#    - Attribute access
#    - Container types emulation
#    - Context managers emulation
#    - Callable objects emulation
# - http://docs.python.org/2.7/reference/datamodel.html#basic-customization
#===============================================================================


# Let's customize our class rich comparison
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

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

fract1 = MyFraction(5, 2)  # 2.5
fract2 = MyFraction(3, 2)  # 1.5
fract3 = MyFraction(25, 10)  # 2.5

print fract1 != fract3  # 2.5 != 2.5
print fract1 == fract3  # 2.5 == 2.5
print fract2 < fract3  # 1.5 < 2.5

# Let's try the other way
print fract1 >= fract2   # 2.5 >= 1.5
print fract2 >= fract3  # 1.5 >= 2.5

# Let's try with other types
print fract1 >= 2  # 2.5 >= 2
print fract2 == 1.5  # 1.5 == 1.5

# Let's try the other way with other types
print 2 <= fract1  # 2 <= 2.5
print 1.5 == fract2   # 1.5 == 1.5


#===============================================================================
# - You don't have to define all the possible methods, Python can take the opposite
# - Python will try the opposite when a comparison method of a type raises TypeError
# - It's up to you to implement compatibility with other types
#===============================================================================


# Let's try again
print 10 > fract1  # 10 > 2.5
print 10 < fract1  # 10 < 2.5
print fract1 < 10  # 2.5 < 10
print fract1 > 10  # 2.5 > 10


# Let's define all comparison methods
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

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

fract1 = MyFraction(5, 2)  # 2.5

print 10 > fract1  # 10 > 2.5
print 10 < fract1  # 10 < 2.5
print fract1 < 10  # 2.5 < 10
print fract1 > 10  # 2.5 > 10


#===============================================================================
# - You don't have to define all the possible methods, Python can take the opposite
#    - But you should do it to support other types!
# - Python will try the opposite when a comparison method of a type raises TypeError
# - It's up to you to implement compatibility with other types
#===============================================================================


# Let's define all comparison methods
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

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
print 7.254 > f1


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

#===============================================================================
# MORE INFO:
# - http://docs.python.org/2.7/reference/datamodel.html#special-method-names
# - http://www.python.org/doc/newstyle/
# - http://www.python.org/download/releases/2.2.3/descrintro/
#===============================================================================
