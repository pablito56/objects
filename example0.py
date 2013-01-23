#-*- coding: utf-8 -*-
u'''
EXAMPLE 0: Objects: type, id, value, mutable vs. immutable
'''


# Let's instantiate a string and check its id, type and value
inst = 'abcd'
print id(inst)
print type(inst)
print inst


# Let's compare the ids of two ints
inst = 12345; print inst is 12345  # Done in one line due to std lib 'code' module issues with ids


#===============================================================================
# - Every object has an identity (its address), a type and a value
# - Use 'id' and 'is' to retrieve or compare the id of an object
# - The interpreter reuses values
#===============================================================================


# Let's do the same with lists
inst = []; print inst is []


# WTF!? Let's try again with ints
inst_int_1 = 12345; inst_int_2 = 12345
print id(inst_int_1), 'vs.', id(inst_int_2)

# Ok. Let's try again with other types
inst_list_1 = []; inst_list_2 = []
inst_none = None
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
# WARNING!
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
inst_A.list_inst.extend([5, 7, 9])
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
## EXERCISE 0: Solve common mutable types usage errors
## - Go to exercices/exercise_0 and edit exercise_0.py
## - Change the functions and class implementation to let tests_0.py pass
## - Check tests with nosetests
##===============================================================================
##===============================================================================

# Wrong multiple assignment of mutables
def split_even_odd(numbers):
    even = odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd

print split_even_odd(range(0, 11))

# Solution multiple assignment of mutables: avoid them
def split_even_odd(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd

print split_even_odd(range(0, 11))


# Wrong class attributes of mutable type 
class NumbersList(object):
    even = []
    odd = []

    def append_number(self, num):
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)

num_lst_A = NumbersList()
num_lst_A.append_number(7)
num_lst_B = NumbersList()
print num_lst_B.even, num_lst_B.odd

# Solution mutable as class attribute: instantiate in the __init__
class NumbersList(object):
    even = None
    odd = None

    def __init__(self):
        self.even = []
        self.odd = []

    def append_number(self, num):
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)

num_lst_A = NumbersList()
num_lst_A.append_number(7)
num_lst_B = NumbersList()
print num_lst_B.even, num_lst_B.odd


# Wrong mutable as function default value
def update_even_odd(numbers, even=[], odd=[]):
    '''Update incoming even and odd numbers lists with corresponding values of numbers iterable
    :param numbers: iterable with numbers
    :return (even, odd) lists with corresponding values
    '''
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd

print update_even_odd(range(0, 11))
print update_even_odd(range(100, 111))

# Solution mutable as function default value: use None as default value and instantiate inside the function
def update_even_odd(numbers, even=None, odd=None):
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

print update_even_odd(range(0, 11))
print update_even_odd(range(100, 111))


#===============================================================================
# To sum up, mutable and immutable types common errors and solution:
# - Multiple assignment --> Avoid multiple assignment of mutable types
#    - The same applies with shallow copy or constructor by copy --> Use copy.deepcopy
# - Class attributes --> Instantiate in the __init__
# - Functions parameters default value --> Use None as default value and instantiate inside the function
#===============================================================================

#===============================================================================
# MORE INFO:
# - http://docs.python.org/2.7/reference/datamodel.html#objects-values-and-types
#===============================================================================
