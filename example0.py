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
# - Mutable and immutable types behavior differences can lead to some common errors!!
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
# Mutable and immutable types common errors:
# - Multiple assignments
#===============================================================================


# Use mutable types as class attributes
class MutablesClass(object):
    list_inst = []
    int_inst = 0

# Let's instantiate the class twice
inst_A = MutablesClass()
inst_B = MutablesClass()


# Let's change one of the instances and check the other instance values
inst_A.int_inst += 1
inst_A.list_inst.append(1)
print inst_B.int_inst
print inst_B.list_inst
print inst_A.list_inst is inst_B.list_inst


#===============================================================================
# Mutable and immutable types common errors:
# - Multiple assignment
# - Class attributes
#===============================================================================


# Let's create a function which returns a modified list
def add_to_list(item, lst=[]):
    lst.append(item)
    return lst

# Let's call this function twice 
result1 = add_to_list(1)
result2 = add_to_list(2)
print result1 is result2
print result1, 'vs', result2


#===============================================================================
# Mutable and immutable types common errors:
# - Multiple assignment
# - Class attributes
# - Functions parameters default value
#===============================================================================


##===============================================================================
##===============================================================================
## TIME TO START WORKING!
##
## EXERCISE 0:
## - Go to exercices/exercise_0 and edit exercise_0.py
## - Change the functions and class implementation to let tests_0.py pass
## - You have to solve these common errors
## - Check with nosetests
##===============================================================================
##===============================================================================

# Solution multiple assignment of mutables
def split_even_odd(numbers):
    '''Split incoming numbers iterable in two lists with even and odd numbers
    :param numbers: iterable with numbers
    :return (even, odd) lists with corresponding values
    '''
    even = []
    odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd


# Solution mutable as class attribute
class NumersList(object):
    '''Class which handles even and odd numbers lists
    '''
    even = None
    odd = None

    def __init__(self):
        self.even = []
        self.odd = []

    def append_number(self, num):
        '''Add a number to its corresponding list (even or odd)
        '''
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)


# Solution mutable as function default value
def update_even_odd(numbers, even=None, odd=None):
    '''Update incoming even and odd numbers lists with corresponding values of numbers iterable
    :param numbers: iterable with numbers
    :return (even, odd) lists with corresponding values
    '''
    if even is None:
        even = []
    if odd is None:
        odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd


#===============================================================================
# Mutable and immutable types common errors:
# - Multiple assignment --> Avoid multiple assignment of mutable types
#    - The same applies with shallow copy or constructor by copy --> Use copy.deepcopy
# - Class attributes --> Instantiate in the __init__
# - Functions parameters default value --> Use None as default value and instantiate inside the function
#===============================================================================
