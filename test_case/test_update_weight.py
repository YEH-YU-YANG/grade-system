import unittest
from unittest.mock import patch
import sys 
sys.path.append("..") 
from gradeSystem import ScoreSystem

class TestBasicUpdateWeight(unittest.TestCase):
    """
    Test function: 
        object.update_weights()
    
    Test description:
        This test suite specifically tests the 'update_weights' function.
        
        The default weights are:
        - 'lab1': 0.1
        - 'lab2': 0.1
        - 'lab3': 0.1
        - 'mid_term': 0.3
        - 'final_exam': 0.4
         
    """
    
    def setUp(self):
        """
        Method description:
            initializes the ScoreSystem object and assigns it to self.system so that it can be used in the test methods.
        """
        self.system = ScoreSystem()
    
    def shortDescription(self):
        """
        Method description:
            Override the shortDescription method to prevent displaying test method descriptions.
        """
        return None
    
    def test_1(self):
        """
        Test description:
            This test case verifies the behavior of 'update_weights' when the input format is 'lab1 30%'.

        Expected behavior:
            The 'lab1' weight should be updated to 0.3, and other weights remain unchanged.
        """
        test_input = "lab1 30%"  
        self.system.update_weights(test_input)
        expected_weights = {
            'lab1': 0.3,
            'lab2': 0.1,
            'lab3': 0.1,
            'mid_term': 0.3,
            'final_exam': 0.4,   
        }
        self.assertDictEqual(self.system.weights, expected_weights)
    
    def test_2(self):
        """
        Test description:
            This test case verifies the behavior of 'update_weights' when the input format is 'lab1 30'.

        Expected behavior:
            The 'lab1' weight should be updated to 0.3, and other weights remain unchanged.
        """
        test_input = "lab1 30"
        self.system.update_weights(test_input)
        expected_weights = {
            'lab1': 0.3,
            'lab2': 0.1,
            'lab3': 0.1,
            'mid_term': 0.3,
            'final_exam': 0.4,   
        }
        self.assertDictEqual(self.system.weights, expected_weights)
        
    def test_3(self):
        """
        Test description:
            This test case verifies the behavior of 'update_weights' when the input format is 'lab1 0.3'.

        Expected behavior:
            The 'lab1' weight should be updated to 0.3, and other weights remain unchanged.
        """
        test_input = "lab1 0.3"
        self.system.update_weights(test_input)
        expected_weights = {
            'lab1': 0.3,
            'lab2': 0.1,
            'lab3': 0.1,
            'mid_term': 0.3,
            'final_exam': 0.4,   
        }
        self.assertDictEqual(self.system.weights, expected_weights) 
    def test_4(self):
        """
        Test description:
            This test case verifies the behavior of 'update_weights' when the input contains leading / trailing spaces.

        Expected behavior:
            The 'lab1' weight should be updated to 0.3, and other weights remain unchanged.
        """
        test_input = (" ")*50 + "lab1 0.3" + (" ")*50
        self.system.update_weights(test_input)
        expected_weights = {
            'lab1': 0.3,
            'lab2': 0.1,
            'lab3': 0.1,
            'mid_term': 0.3,
            'final_exam': 0.4,   
        }
        self.assertDictEqual(self.system.weights, expected_weights) 
class TestHardUpdateWeight(unittest.TestCase):
    """
    Test function: 
        object.update_weights()
    
    Test description:
        This test suite specifically tests the 'update_weights' function.
        
        The default weights are:
        - 'lab1': 0.1
        - 'lab2': 0.1
        - 'lab3': 0.1
        - 'mid_term': 0.3
        - 'final_exam': 0.4
         
    """
    def setUp(self):
        """
        Method description:
            initializes the ScoreSystem object and assigns it to self.system so that it can be used in the test methods.
        """
        self.system = ScoreSystem()
    
    def shortDescription(self):
        """
        Method description:
            Override the shortDescription method to prevent displaying test method descriptions.
        """
        return None
    
    def test_1(self):
        """
        Test description:
            This test case verifies the behavior of 'update_weights' when the input string includes percentage values, decimals, and integers.

        Expected behavior:
            The 'lab1' weight should be updated to 0.2, 'lab2' to 0.12, 'lab3' to 0.5, 'mid_term' to 0 and 'final_exam' to 0.33.

        """
        test_input = "lab1 20% lab2 12 lab3 0.5 mid_term 0.0 final_exam 33 "
        self.system.update_weights(test_input)
        expected_weights = {
            'lab1': 0.2,
            'lab2': 0.12,
            'lab3': 0.5,
            'mid_term': 0,
            'final_exam': 0.33
        }
        self.assertDictEqual(self.system.weights, expected_weights)

    def test_2(self):
        test_input = "lab2 10 final_exam 0.33 lab1 20% lab3 0.5"
        self.system.update_weights(test_input)
        expected_weights = {
            'lab1': 0.2,
            'lab2': 0.1,
            'lab3': 0.5,
            'mid_term': 0.3,
            'final_exam': 0.33
        }
        self.assertDictEqual(self.system.weights, expected_weights)
    
    def test_3(self):
        test_input = "lab1 20% lab2 70 lab3 0.5 final_exam 0.33"
        self.system.update_weights(test_input)
        expected_weights = {
            'lab1': 0.2,
            'lab2': 0.7,
            'lab3': 0.5,
            'mid_term': 0.3,
            'final_exam': 0.33,   
        }
        self.assertDictEqual(self.system.weights, expected_weights)
    
    def test_4(self):
        test_input = "mid_term 10 lab1 0.2 final_exam 35% lab2 25"
        self.system.update_weights(test_input)
        expected_weights = {
            'lab1': 0.2,
            'lab2': 0.25,
            'lab3': 0.1,
            'mid_term': 0.1,
            'final_exam': 0.35,   
        }
        self.assertDictEqual(self.system.weights, expected_weights)
        
# if __name__ == '__main__':
    
#     """
#     全部 Class 的 test case 一起測
#     """

#     unittest.main()