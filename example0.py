#-*- coding: utf-8 -*-
u'''
EXAMPLE 0: Objects: type, id and value
'''


# Let's instantiate an int and check its id, type and value
inst = 'abcd'
print id(inst)
print type(inst)
print inst


# Let's compare the ids of two ints
inst = 12345; print inst is 12345  # Done in one line due to 'code' module issues with ids


#===============================================================================
# - Every object has an identity (its address), a type and a value
# - Use 'id' and 'is' to retrieve or compare the id of an object
# - The interpreter reuses values
#===============================================================================


# Let's do the same with lists
inst = []; print inst is []


# WTF!? Let's try again
inst_int_1 = 12345; inst_int_2 = 12345
inst_list_1 = []; inst_list_2 = []
inst_none = None
print id(inst_int_1), 'vs.', id(inst_int_2)
print id(inst_list_1), 'vs.', id(inst_list_2)
print id(inst_none), 'vs.', id(None)


#===============================================================================
# - Objects whose value can change are said to be mutable (dicts, lists)
# - Objects whose value is unchangeable once they are created are called immutable (numbers, strings, tuples)
# - Mutable types allow in-place modifications (append in a list, pop in a dictionary...)
# - Immutable types values are reused by the interpreter (so their id is the same)
#===============================================================================


# Let's change (reassign) a string value
inst = 'instance value'
print inst, '@', id(inst)
inst = inst + ' updated'
print inst, '@', id(inst)


# Let's update a list content
inst = ['instance', 'value']
print inst, '@', id(inst)
inst.append('updated')
print inst, '@', id(inst)


# Now let's play with dicts
dict1 = {(1, 2): "1, 2", (3, 4): "3, 4"}
try:
    dict2 = {[1, 2]: "1, 2", [3, 4]: "3, 4"}
except TypeError, e:
    print e.__class__.__name__, e


#===============================================================================
# - Mutable types are not stable, so they can not be used as dict keys
#===============================================================================


#===============================================================================
# This can lead to some common errors!!
#===============================================================================


# Multiple assignment with ints (immutable)
intA = intB = 0
print intA, '@', id(intA)
print intB, '@', id(intB)


# Let's modify one of the ints
intA += 1
print intA, '@', id(intA)
print intB, '@', id(intB)


# Ok. Multiple assignment with lists (mutable)
lstA = lstB = []
print lstA, '@', id(lstA)
print lstB, '@', id(lstB)


# Let's modify one of the lists
lstA.extend([1, 2, 3])
print lstA, '@', id(lstA)
print lstB, '@', id(lstB)


#===============================================================================
# Mutable and immutabel types common errors:
# - Multiple assignment --> Avoid multiple assignment of mutable types!
#    - The same applies with shallow copy or constructor by copy --> Use copy.deepcopy 
# - Class attributes
#===============================================================================


# Use mutable types as class attributes
class MutablesClass(object):
    list_inst = []
    int_inst = 0

inst1 = MutablesClass()
inst2 = MutablesClass()


# Let's change one of the instances of my class and check the other instance
inst1.list_inst.append(1)
inst1.int_inst += 1
print inst2.list_inst
print inst2.int_inst


#===============================================================================
# Mutable and immutabel types common errors:
# - Multiple assignment --> Avoid multiple assignment of mutable types
#    - The same applies with shallow copy or constructor by copy --> Use copy.deepcopy 
# - Class attributes --> Instantiate in the __init__ !
# - Functions parameters default value
#===============================================================================


# Let's create and call a method
def add_to_list(item, lst=[]):
    lst.append(item)
    return lst

result1 = add_to_list(1)
result2 = add_to_list(2)
print result1 is result2
print result1, 'vs', result2


#===============================================================================
# Mutable and immutabel types common errors:
# - Multiple assignment --> Avoid multiple assignment of mutable types
#    - The same applies with shallow copy or constructor by copy --> Use copy.deepcopy 
# - Class attributes --> Instantiate in the __init__
# - Functions parameters default value --> Use None as default value and instantiate inside the function ! 
#===============================================================================
