import unittest
from unittest.mock import patch
import sys 
sys.path.append("..") 
from gradeSystem import ScoreSystem


class TestUpdateGrade(unittest.TestCase):
    """
    Test suite for the update_grade method in the ScoreSystem class.
    
    Attributes:
        system : An instance of the ScoreSystem class initialized for testing.

    Methods:
        setUp: Initializes the ScoreSystem object and assigns it to self.system for use in test methods.
        tearDown: Cleans up the ScoreSystem object after each test.
        shortDescription: Prevent displaying test method descriptions.
        test_valid_input: Tests the update_grade method with various valid input formats.
        test_invalid_input: Tests the update_grade method with various invalid input formats.
    """
    def setUp(self):
        """
        Method description:
            initializes the ScoreSystem object and assigns it to self.system so that it can be used in the test methods.
        """
        self.system = ScoreSystem()
        self.system.load_input_data()
        
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
    def test_valid_input(self, mock_input):
        """
        Test description:
            This test suite verifies the behavior of 'update_grade' method in the ScoreSystem class 
            with various valid input formats.

        Test cases:
            Each test case includes an id, input, and expected_grades string representing the student's ID, 
            modified grades, and the expected resulting grades.

        Expected behavior:
            For each test case, student's grades should match the expected grades.

        """
        
        test_cases = [
            { 'id': '955002056', 'input': 'lab1 80'                                                 , 'expected_grades': { 'lab1': 80 , 'lab2': 92 , 'lab3': 88 , 'mid_term': 98 , 'final_exam': 91  } },
            { 'id': '955002056', 'input': 'lab2 70'                                                 , 'expected_grades': { 'lab1': 80 , 'lab2': 70 , 'lab3': 88 , 'mid_term': 98 , 'final_exam': 91  } },
            { 'id': '955002056', 'input': 'lab3 50'                                                 , 'expected_grades': { 'lab1': 80 , 'lab2': 70 , 'lab3': 50 , 'mid_term': 98 , 'final_exam': 91  } },
            { 'id': '955002056', 'input': 'mid_term 100'                                            , 'expected_grades': { 'lab1': 80 , 'lab2': 70 , 'lab3': 50 , 'mid_term': 100, 'final_exam': 91  } },
            { 'id': '955002056', 'input': 'final_exam 90'                                           , 'expected_grades': { 'lab1': 80 , 'lab2': 70 , 'lab3': 50 , 'mid_term': 100, 'final_exam': 90  } },
            { 'id': '955002056', 'input': 'lab1 100 lab2 100 lab3 100 mid_term 100 final_exam 100'  , 'expected_grades': { 'lab1': 100, 'lab2': 100, 'lab3': 100, 'mid_term': 100, 'final_exam': 100 } },
            { 'id': '955002056', 'input': 'final_exam 100  mid_term 100 lab3 100 lab2 100 lab1 100' , 'expected_grades': { 'lab1': 100, 'lab2': 100, 'lab3': 100, 'mid_term': 100, 'final_exam': 100 } }
        ]
        
        for test_case in test_cases:
            id = test_case["id"]
            input_value = test_case["input"]
            expected_grades = test_case["expected_grades"]
            with self.subTest((id,input_value, expected_grades)):
                mock_input.side_effect = [id, input_value]
                self.system.update_grade()
                if id in self.system.student:
                    result = self.system.student[id]['scores']
                else:
                    result = {}
                self.assertDictEqual(result, expected_grades)    
        
    @patch('builtins.input')
    def test_invalid_input(self, mock_input):
        """
        Test description:
            This test suite verifies the behavior of 'update_grade' method in the ScoreSystem class 
            with various invalid input formats.

        Test cases:
            Each test case includes an input string representing weight updates and the expected resulting weights.

        Expected behavior:
            For each test case, the system weights should match the expected weights.

        """
        
        test_cases = [
           { 'id': '1'        , 'input': 'final_exam 100  mid_term 100 lab3 100 lab2 100 lab1 100' , 'expected_grades': {} },  
           { 'id': '?.@\()dsa', 'input': 'final_exam 100  mid_term 100 lab3 100 lab2 100 lab1 100' , 'expected_grades': {} },  
           { 'id': ''         , 'input': 'final_exam 100  mid_term 100 lab3 100 lab2 100 lab1 100' , 'expected_grades': {} },  
           { 'id': '  '       , 'input': 'final_exam 100  mid_term 100 lab3 100 lab2 100 lab1 100' , 'expected_grades': {} },  
           { 'id': '\t\n  '   , 'input': 'final_exam 100  mid_term 100 lab3 100 lab2 100 lab1 100' , 'expected_grades': {} },  
           { 'id': '955002056', 'input': 'alskjalwwjriqq as;da;koe pd as;ka;' , 'expected_grades': { 'lab1': 88 , 'lab2': 92 , 'lab3': 88 , 'mid_term': 98 , 'final_exam': 91  } }
        ]
        
        for test_case in test_cases:
            id = test_case["id"]
            input_value = test_case["input"]
            expected_grades = test_case["expected_grades"]
            with self.subTest((id,input_value, expected_grades)):
                mock_input.side_effect = [id, input_value]
                self.system.update_grade()
                if id in self.system.student:
                    result = self.system.student[id]['scores']
                else:
                    result = {}
                self.assertDictEqual(result, expected_grades)