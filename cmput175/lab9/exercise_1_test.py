import unittest
from exercise_1 import *
import random

class TestEx1(unittest.TestCase):

    def test_empty_array(self):
        input_array=[]
        recursive_selection_sort(input_array,0)
        self.assertEqual(input_array,[])
        
    def test_one_element(self):
        input_array=[0]
        recursive_selection_sort(input_array,1)
        self.assertEqual(input_array,[0])
        
    def test_in_and_out_of_order(self):
        input_array=[3,2,1]
        recursive_selection_sort(input_array,3)
        self.assertEqual(input_array,[3,2,1])
        
        input_array=[1,2,3]
        recursive_selection_sort(input_array,3)
        self.assertEqual(input_array,[3,2,1])
        
    def test_repeated_elements(self):
        input_array=[3,1,1,5]
        recursive_selection_sort(input_array,4)
        self.assertEqual(input_array,[5,3,1,1])
        
    def test_mixed_numbers(self):
        input_array=[2,-5,0,3,-2,4]
        recursive_selection_sort(input_array,6)
        self.assertEqual(input_array,[4,3,2,0,-2,-5])
        
    def test_random_numbers(self):
        input_array = [random.randint(1,1000) for i in range(500)]
        sorted_list = sorted(input_array, reverse=True)
        recursive_selection_sort(input_array,500)
        self.assertEqual(input_array,sorted_list)


if  __name__== "__main__":
    unittest.main()

