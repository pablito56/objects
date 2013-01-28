#-*- coding: utf-8 -*-
u'''
Test exercise 0: mutable and immutable types common errors
'''
import unittest
import exercise_1 as source
# import solution_1 as source


class VerboseTestCase(unittest.TestCase):
    '''Base unit tests class for verbose output
    '''
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.longMessage = True


class TestNewStyle(VerboseTestCase):
    '''Test exercise 1: new-style classes
    '''
    def test_old_style_inheritance(self):
        '''Check inheritance from old-style classes
        '''
        custom_parser = source.CustomOptionParser()
        self.assertEqual(type(custom_parser), custom_parser.__class__, "Type and class difer in CustomOptionParser")


class TestCustomOrderedDict(VerboseTestCase):
    '''Test exercise 2: data model
    '''
    def test_str(self):
        vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU"))
        #=======================================================================
        # CustomOrderedDict([('a', 'A'), ('e', 'E'), ('i', 'I'), ('o', 'O'), ('u', 'U')])
        #=======================================================================
        expected = "{'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}"
        expected2 = "{'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U', 1: 1}"
        self.assertEqual(str(vowels),  expected, "Wrong str in CustomOrderedDict")
        vowels[1] = 1
        self.assertEqual(str(vowels),  expected2, "Wrong str in CustomOrderedDict")

    #===========================================================================
    # def test_get_item(self):
    #    vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU"))
    #    #=======================================================================
    #    # CustomOrderedDict([('a', 'A'), ('e', 'E'), ('i', 'I'), ('o', 'O'), ('u', 'U')])
    #    #=======================================================================
    #    self.assertEqual(vowels[2], "I", "Wrong index access in CustomOrderedDict")
    #    self.assertEqual(vowels[-2], "O", "Wrong negative index access in CustomOrderedDict")
    #===========================================================================

    def test_slicing(self):
        vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU"))
        #=======================================================================
        # CustomOrderedDict([('a', 'A'), ('e', 'E'), ('i', 'I'), ('o', 'O'), ('u', 'U')])
        #=======================================================================
        slice_vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU")[2:4])
        #=======================================================================
        # CustomOrderedDict([('i', 'I'), ('o', 'O')])
        #=======================================================================
        self.assertEqual(vowels[2:4], slice_vowels, "Wrong slicing in CustomOrderedDict")
        self.assertEqual(vowels[2:-1], slice_vowels, "Wrong slicing in CustomOrderedDict")
        self.assertEqual(vowels[2:-10], source.CustomOrderedDict(), "Wrong slicing in CustomOrderedDict")

    def test_addition(self):
        vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU"))
        #=======================================================================
        # CustomOrderedDict([('a', 'A'), ('e', 'E'), ('i', 'I'), ('o', 'O'), ('u', 'U')])
        #=======================================================================
        letters = zip("aixy", ["AA", "II", "XX", "Y"])
        expected = source.CustomOrderedDict(zip("aeiouxy", ["AA", "E", "II", "O", "U", "XX", "Y"]))
        #=======================================================================
        # CustomOrderedDict([('a', 'AA'), ('e', 'E'), ('i', 'II'), ('o', 'O'), ('u', 'U'), ('x', 'XX'), ('y', 'Y')])
        #=======================================================================
        self.assertEqual(vowels + letters, expected, "Wrong addition in CustomOrderedDict (list)")
        self.assertEqual(vowels + source.CustomOrderedDict(letters), expected, "Wrong addition in CustomOrderedDict (CustomOrderedDict)")
        self.assertEqual(vowels, source.CustomOrderedDict(zip("aeiou", "AEIOU")), "Wrong addition in CustomOrderedDict (modified self)")

    def test_substraction(self):
        vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU"))
        #=======================================================================
        # CustomOrderedDict([('a', 'A'), ('e', 'E'), ('i', 'I'), ('o', 'O'), ('u', 'U')])
        #=======================================================================
        letters = "aixy"
        letters_cod = source.CustomOrderedDict(zip("aixy", ["AA", "II", "XX", "Y"]))
        expected = source.CustomOrderedDict(zip("eou", ["E", "O", "U"]))
        #=======================================================================
        # CustomOrderedDict([('a', 'AA'), ('e', 'E'), ('i', 'II'), ('o', 'O'), ('u', 'U'), ('x', 'XX'), ('y', 'Y')])
        #=======================================================================
        self.assertEqual(vowels - letters, expected, "Wrong substraction in CustomOrderedDict (list)")
        self.assertEqual(vowels - letters_cod, expected, "Wrong substraction in CustomOrderedDict (CustomOrderedDict)")
        self.assertEqual(vowels, source.CustomOrderedDict(zip("aeiou", "AEIOU")), "Wrong substraction in CustomOrderedDict (modified self)")
    

#===============================================================================
#    def test_append_number_even(self):
#        '''Check mutable class attributes
#        '''
#        inst = exercise_0.NumbersList()
#        number = 6
#        expected_even = [number]
#        expected_odd = []
#        inst.append_number(number)
#        self.assertEqual(inst.even, expected_even, "Even values differ")
#        self.assertEqual(inst.odd, expected_odd, "Odd values differ")
# 
#    def test_append_number_odd(self):
#        '''Check mutable as class attributes
#        '''
#        inst = exercise_0.NumbersList()
#        number = 7
#        expected_even = []
#        expected_odd = [number]
#        inst.append_number(number)
#        self.assertEqual(inst.even, expected_even, "Even values differ")
#        self.assertEqual(inst.odd, expected_odd, "Odd values differ")
# 
#    def test_update_even_odd_I(self):
#        '''Check mutable as default value I
#        '''
#        numbers = range(0, 16)
#        expected_even = range(0, 16, 2)
#        expected_odd = range(1, 16, 2)
#        even, odd = exercise_0.update_even_odd(numbers)
#        self.assertEqual(even, expected_even, "Even values differ")
#        self.assertEqual(odd, expected_odd, "Odd values differ")
# 
#    def test_update_even_odd_II(self):
#        '''Check mutable as default value II
#        '''
#        numbers = range(1, 17)
#        expected_even = range(2, 17, 2)
#        expected_odd = range(1, 17, 2)
#        even, odd = exercise_0.update_even_odd(numbers)
#        self.assertEqual(even, expected_even, "Even values differ")
#        self.assertEqual(odd, expected_odd, "Odd values differ")
#===============================================================================


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
