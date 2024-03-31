import unittest
from unittest.mock import patch
import sys 
sys.path.append("..") 
from gradeSystem import ScoreSystem


class TestAddStudent(unittest.TestCase):
    """
    Test suite for the add_student method in the ScoreSystem class.
    
    Attributes:
        system : An instance of the ScoreSystem class initialized for testing.

    Methods:
        setUp: Initializes the ScoreSystem object and assigns it to self.system for use in test methods.
        tearDown: Cleans up the ScoreSystem object after each test.
        shortDescription: Prevent displaying test method descriptions.
        test_valid_input: Tests the add_student method with various valid input formats.
        test_invalid_input: Tests the add_student method with various invalid input formats.
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
            Each test case includes an id, name, input, expected_data  
            representing the student's ID, student's NAME, student's grades, and corresponding student's data in JSON format
            
        Expected behavior:
            For each test case, result should match the expected_data.
        """
        test_cases = [
            {'id': '1', 'name': "Ale" , 'input':'lab1 70 lab2 90 lab3 100 mid_term 60 final_exam 55', 'expected_result':{'name':'Ale' , 'scores':{'lab1':70,'lab2':90,'lab3':100,'mid_term':60,'final_exam':55}}},
            {'id': '2', 'name': "Rusy", 'input':'final_exam 55 mid_term 60 lab3 100 lab2 90 lab1 70', 'expected_result':{'name':'Rusy', 'scores':{'lab1':70,'lab2':90,'lab3':100,'mid_term':60,'final_exam':55}}},
            {'id': '3', 'name': "Dine", 'input':''                                                  , 'expected_result':{'name':'Dine', 'scores':{'lab1':0 ,'lab2':0 ,'lab3':0  ,'mid_term':0 ,'final_exam':0 }}},
        ]
        
        for test_case in test_cases:
            id, name, input_grades, expected_result = test_case.values()
            with self.subTest((id, name, input_grades, expected_result)):
                mock_input.side_effect = [id, name, input_grades]
                if id in self.system.student: 
                    mock_input.side_effect = [id]
                else: 
                    mock_input.side_effect = [id, name, input_grades]
                self.system.add_student()
                result = self.system.student[id]
                self.assertDictEqual(result, expected_result)  
                
    @patch('builtins.input')
    def test_invalid_input(self, mock_input):
        """
        Test description:
            This test suite verifies the behavior of 'update_grade' method in the ScoreSystem class 
            with various invalid input formats.

        Test cases:
            Each test case includes an id, name, input, expected_data  
            representing the student's ID, student's NAME, student's grades, and corresponding student's data in JSON format
            
        Expected behavior:
            For each test case, result should match the expected_data.
        """
        test_cases = [
            {'id': '1', 'name': "Ale" , 'input':'lab1 70 lab2 90 lab3 100 mid_term 60 final_exam 55', 'expected_result':{'name':'Ale' , 'scores':{'lab1':70,'lab2':90,'lab3':100,'mid_term':60,'final_exam':55}}},
            {'id': '1', 'name': "Sony", 'input':'lab1 80'                                           , 'expected_result':{'name':'Ale' , 'scores':{'lab1':70,'lab2':90,'lab3':100,'mid_term':60,'final_exam':55}}},
            {'id': '1', 'name': "Ale ", 'input':'lab1 80 lab3 70 mid_term 90'                       , 'expected_result':{'name':'Ale' , 'scores':{'lab1':70,'lab2':90,'lab3':100,'mid_term':60,'final_exam':55}}},
        
        ]
        
        for test_case in test_cases:
            id, name, input_grades, expected_result = test_case.values()
            with self.subTest((id, name, input_grades, expected_result)):
                mock_input.side_effect = [id, name, input_grades]
                if id in self.system.student: 
                    mock_input.side_effect = [id]
                else: 
                    mock_input.side_effect = [id, name, input_grades]
                self.system.add_student()
                result = self.system.student[id]
                self.assertDictEqual(result, expected_result)  
    
