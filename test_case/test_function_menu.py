import unittest
from unittest.mock import patch
import sys 
sys.path.append("..") 
from gradeSystem import ScoreSystem
from gradeSystem import Method

class TestFunctionMenu(unittest.TestCase):
    """
    Test suite for the 'function menu & exit' method in the ScoreSystem class.
    
    Attributes:
        system : An instance of the ScoreSystem class initialized for testing.

    Methods:
        setUp: Initializes the ScoreSystem object and assigns it to self.system for use in test methods.
        tearDown: Cleans up the ScoreSystem object after each test.
        shortDescription: Prevent displaying test method descriptions.
        test_valid_input: Tests the 'function menu & exit' method with various valid input.
        test_invalid_input: Tests the 'function menu & exit' method with various invalid input.
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
            Verifies the behavior of 'function menu & exit' method with various valid input formats.

        Test cases:
            Each test case includes test, score, and expected_result 
            representing  the test name (lab1, lab2 ...), score as threshold, and the correct filtered student data.

        Expected behavior:
            For each test case, result of 'function menu & exit' method should match the expected result.
        """
        test_cases = [
            { 'input_value': ['1' , 'None'     , Method.EXIT.value], 'expected_result': Method.SHOW_SCORE.value        },
            { 'input_value': ['2' , 'None'     , Method.EXIT.value], 'expected_result': Method.SHOW_GRADE_LETTER.value },
            { 'input_value': ['3' , 'None'     , Method.EXIT.value], 'expected_result': Method.SHOW_AVERAGE.value      },
            { 'input_value': ['4' , 'None'     , Method.EXIT.value], 'expected_result': Method.SHOW_RANK.value         },
            # { 'input_value': ['5' , 'None'     , Method.EXIT.value], 'expected_result': Method.SHOW_DISTRIBUTION.value },
            { 'input_value': ['6' , 'None'     , Method.EXIT.value], 'expected_result': Method.FILTERING.value         },
            { 'input_value': ['7' , '955002056', Method.EXIT.value], 'expected_result': Method.ADD_STUDENT.value       },
            { 'input_value': ['8' , 'None'     , Method.EXIT.value], 'expected_result': Method.UPDATE_GRADE.value      },
            { 'input_value': ['9' , 'None'     , Method.EXIT.value], 'expected_result': Method.UPDATE_WEIGHTS.value    },
            { 'input_value': ['11', Method.EXIT.value]             , 'expected_result': Method.INVALID.value           }
        ]
        for test_case in test_cases:
            input_value, expected_result = test_case.values()
            with self.subTest((input_value, expected_result)):
                mock_input.side_effect = input_value
                self.system.function_menu_and_exit()
                self.assertEqual(self.system.method_call_value, expected_result)

                
