#-*- coding: utf-8 -*-
###
# MODULE 04: creation and instantiation: __new__ and metaclasses
###


class VerboseCreator(object):
    def __new__(cls, *args, **kwargs):
        print "__new__", cls, args, kwargs
        res = super(VerboseCreator, cls).__new__(cls, *args, **kwargs)
        print "type:", type(res)
        return res

    def __init__(self, *args, **kwargs):
        print "__init__", self, args, kwargs
        super(VerboseCreator, self).__init__(*args, **kwargs)

verb_inst = VerboseCreator()


#===============================================================================
# - __new__ is a special static method called to create a new instance of the class
#    - No need to be defined as static
#    - Called when you 'call' the class
# - It takes the class as first argument followed by all object constructor arguments
# - It returns the new instance
#    - Later __init__ will be called on that instance
# - When calling __new__ with super, the class must be provided as first parameter
#===============================================================================


class VerboseCreatorDict(VerboseCreator, dict):
    pass

verb_dict_inst = VerboseCreatorDict({'a': 1, 'b': 2})
print verb_dict_inst


# A more real example
class MySingleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(MySingleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst

inst_1 = MySingleton()
inst_2 = MySingleton()
print id(inst_1), 'vs.', id(inst_2)


# Another example
class RoundedFloat(float):
    def __new__(cls, *args, **kwargs):
        if args:
            args = [round(args[0], 2)]
        return super(RoundedFloat, cls).__new__(cls, *args, **kwargs)

print RoundedFloat(7.12345)


#===============================================================================
# Common uses:
#   - Singleton pattern, although the most recommended implementation is using a module
#   - Factory pattern
#   - When subclassing immutable types, to customize the instance creation
#   - In custom metaclasses in order to customise class creation
#===============================================================================


# Metaclasses? What's that?

print type(verb_dict_inst)

print type(type(verb_dict_inst))

print type(VerboseCreatorDict)


#===============================================================================
# - The metaclass is the type of a class.
# - By default new-style classes are constructed using type().
# - A class definition is read into a separate namespace and the value of class name
#   is bound to the result of calling type(name, bases, dict)
#
# More info: http://docs.python.org/2/reference/datamodel.html#customizing-class-creation
#===============================================================================


# A simple example
class MyVerboseMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        print "NEW CLASS:"
        print " - metaclass:", mcs
        print " - name:", name
        print " - bases:", bases
        print " - attrs:", attrs
        new_class = super(MyVerboseMetaclass, mcs).__new__(mcs, name, bases, attrs)
        return new_class


# Let's use this metaclass. Pay attention


class MyMetaclassedClass(object):
    __metaclass__ = MyVerboseMetaclass
    class_attrib = "class attrib value"

    def method(self, *args, **kwargs):
        return True


# Notice how the metaclass acts on import time, when creating the metaclassed class


print MyMetaclassedClass

print type(MyMetaclassedClass)


# Let's see a real example

# Let's implement a logging decorator
def _logging_decorator(func):
    def logging_wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if not res:
            print "CALL FAILED:", args, kwargs,
        return res
    return logging_wrapper


# Let's define a metaclass using it
from inspect import isfunction
def _decorate_attrs(attrs):
    decorated_attrs = {}
    for name, func in attrs.items():
        if isfunction(func):
            func = _logging_decorator(func)
        decorated_attrs[name] = func
    return decorated_attrs

class LoggingMetaclass(type):
    def __new__(mcs, name, bases, attrs):
#        print "NEW", mcs, name, bases, attrs
        new_class = super(LoggingMetaclass, mcs).__new__(mcs, name, bases, _decorate_attrs(attrs))
        return new_class


# Let's use this metaclass
class TrueFalseClass(object):
    __metaclass__ = LoggingMetaclass
    class_attrib = "class attrib value"
    def ret_false(self, *args, **kwargs):
        return False
    def ret_true(self, *args, **kwargs):
        return True


tf_inst = TrueFalseClass()

tf_inst.ret_true()

tf_inst.ret_false()

tf_inst.ret_false(1, "xyz", arg1=7)


#===============================================================================
# Metaclasses usage:
# - Modifying the class dictionary prior to the class being created
# - Returning an instance of another class like a factory pattern
# - Really useful to modify classes (e.g. decorate classes methods) dynamically:
#    - Logging
#    - Timing or profiling
#    - Caching
#    - ...
#
# - It can be specified system-wide with a global variable '__metaclass__'
#===============================================================================


#===============================================================================
# __new__
#    - Intercepts instances creation
#    - Executed on instantiation time
#    - Affects instances one by one
#
# __metaclass__
#    - Intercepts class creation
#    - Executed on import time
#    - Affects all instances at once
#===============================================================================


#===============================================================================
# More info:
# - http://docs.python.org/2/reference/datamodel.html#customizing-class-creation
# - http://www.voidspace.org.uk/python/articles/metaclasses.shtml
#===============================================================================
