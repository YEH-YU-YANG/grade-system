import unittest
from unittest.mock import patch
import sys 
sys.path.append("..") 
from gradeSystem import ScoreSystem

class TestUpdateWeights(unittest.TestCase):

    def setUp(self):
        """
        Method description:
            initializes the ScoreSystem object and assigns it to self.system so that it can be used in the test methods.
        """
        self.system = ScoreSystem()
        
    def tearDown(self):
        """
        Method description:
            Cleans up the ScoreSystem object after each test.
        """
        del self.system
        
    def shortDescription(self):
        """
        Method description:
            Override the shortDescription method to prevent displaying test method descriptions.
        """
        return None
    
    @patch('builtins.input')
    def test_invalid_input(self, mock_input):
        """
        Test description:
            Verifie the behavior of 'update_weights' with various invalid input formats.
        
        Test cases:
            All of test_case ate invalid input data.
        
        Expected behavior:
            System weights should remain unchanged.
        """
        
        test_cases = [
            "lab1 30%",
            "lab1 30",
            "lab1 0.3",
            (" ")*50 + "lab1 0.3" + (" ")*50,
            "lab1 -30%",                
            "lab1 110%",                                            
            "lab1 30% lab2 20%",         
        ]
        
        expected_weights = {
            'lab1': 0.1,
            'lab2': 0.1,
            'lab3': 0.1,
            'mid_term': 0.3,
            'final_exam': 0.4,   
        }
        
        for input_value in test_cases:
            with self.subTest(input_value):
                mock_input.return_value = input_value
                self.system.update_weights()
                self.assertDictEqual(self.system.weights, expected_weights)
    
    @patch('builtins.input')
    def test_valid_input(self, mock_input):
        """
        Test description:
            This test suite verifies the behavior of 'update_weights' method in the ScoreSystem class 
            with various valid input formats.

        Test cases:
            Each test case includes an input string representing weight updates and the expected resulting weights.

        Expected behavior:
            For each test case, the system weights should match the expected weights.

        """
        
        test_cases = [
            { 'input': 'lab1 0 lab2 0 lab3 0 mid_term 0.6'                      , 'expected_weights': { 'lab1': 0  , 'lab2': 0   , 'lab3': 0   , 'mid_term': 0.6, 'final_exam': 0.4  } },
            { 'input': 'lab1 50 lab2 20 lab3 30 mid_term 0 final_exam 0'        , 'expected_weights': { 'lab1': 0.5, 'lab2': 0.2 , 'lab3': 0.3 , 'mid_term': 0  , 'final_exam': 0    } },
            { 'input': 'lab1 10 lab2 10 lab3 10 mid_term 0.3 final_exam 0.4'    , 'expected_weights': { 'lab1': 0.1, 'lab2': 0.1 , 'lab3': 0.1 , 'mid_term': 0.3, 'final_exam': 0.4  } },
            { 'input': 'lab1 0% lab2 0% lab3 0% mid_term 60% final_exam 40%'    , 'expected_weights': { 'lab1': 0  , 'lab2': 0   , 'lab3': 0   , 'mid_term': 0.6, 'final_exam': 0.4  } },
            { 'input': 'lab1 50% lab2 20% lab3 30% mid_term 0% final_exam 0%'   , 'expected_weights': { 'lab1': 0.5, 'lab2': 0.2 , 'lab3': 0.3 , 'mid_term': 0  , 'final_exam': 0    } },
            { 'input': 'lab1 10% lab2 10% lab3 10% mid_term 30% final_exam 40%' , 'expected_weights': { 'lab1': 0.1, 'lab2': 0.1 , 'lab3': 0.1 , 'mid_term': 0.3, 'final_exam': 0.4  } },
            { 'input': 'lab1 0 lab2 0 lab3 0 mid_term 60 final_exam 40'         , 'expected_weights': { 'lab1': 0  , 'lab2': 0   , 'lab3': 0   , 'mid_term': 0.6, 'final_exam': 0.4  } },
            { 'input': 'lab1 50 lab2 20 lab3 30 mid_term 0 final_exam 0'        , 'expected_weights': { 'lab1': 0.5, 'lab2': 0.2 , 'lab3': 0.3 , 'mid_term': 0  , 'final_exam': 0    } },
            { 'input': 'lab1 10 lab2 10 lab3 10 mid_term 30 final_exam 40'      , 'expected_weights': { 'lab1': 0.1, 'lab2': 0.1 , 'lab3': 0.1 , 'mid_term': 0.3, 'final_exam': 0.4  } },
            { 'input': 'lab1 20% lab2 12 lab3 0.3 mid_term 0.0 final_exam 38'   , 'expected_weights': { 'lab1': 0.2, 'lab2': 0.12, 'lab3': 0.3 , 'mid_term': 0  , 'final_exam': 0.38 } },
            { 'input': 'lab1 20% lab2 12 lab3 0.3 mid_term 0.0 final_exam 38'   , 'expected_weights': { 'lab1': 0.2, 'lab2': 0.12, 'lab3': 0.3 , 'mid_term': 0  , 'final_exam': 0.38 } },
            { 'input': 'lab2 10 final_exam 0.33 lab1 20% lab3 0.07 mid_term 30%', 'expected_weights': { 'lab1': 0.2, 'lab2': 0.1 , 'lab3': 0.07, 'mid_term': 0.3, 'final_exam': 0.33 } },
        ]
        
        for test_case in test_cases:
            input_value = test_case["input"]
            expected_weights = test_case["expected_weights"]
            with self.subTest((input_value, expected_weights)):
                mock_input.return_value = input_value
                self.system.update_weights()
                self.assertDictEqual(self.system.weights, expected_weights)
        

        
