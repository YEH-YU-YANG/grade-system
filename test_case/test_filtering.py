import unittest
from unittest.mock import patch
import sys 
sys.path.append("..") 
from gradeSystem import ScoreSystem


class TestFiltering(unittest.TestCase):
    """
    Test suite for the 'filtering' method in the ScoreSystem class.
    
    Attributes:
        system : An instance of the ScoreSystem class initialized for testing.

    Methods:
        setUp: Initializes the ScoreSystem object and assigns it to self.system for use in test methods.
        tearDown: Cleans up the ScoreSystem object after each test.
        shortDescription: Prevent displaying test method descriptions.
        test_valid_input: Tests the 'filtering' method with various valid input.
        test_invalid_input: Tests the 'filtering' method with various invalid input.
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
            Verifies the behavior of 'filtering' method with various valid input formats.

        Test cases:
            Each test case includes test, score, and expected_result 
            representing  the test name (lab1, lab2 ...), score as threshold, and the correct filtered student data.

        Expected behavior:
            For each test case, result of 'filtering' method should match the expected result.
        """
        test_cases = [
            {'test':'lab1'      , 'score':'99'  , 'expected_result': {'test': 'lab1'      ,'datas':['ID: 975002069, Name: 練俊民, lab1\'s grade: 99','ID: 985002002, Name: 林芯妤, lab1\'s grade: 99','ID: 985002014, Name: 王祉鈞, lab1\'s grade: 99','ID: 985002027, Name: 張軒滄, lab1\'s grade: 99','ID: 985002028, Name: 許哲浩, lab1\'s grade: 99','ID: 985002036, Name: 陳健新, lab1\'s grade: 99','ID: 985002038, Name: 吳德毅, lab1\'s grade: 99']}},
            {'test':'lab1'      , 'score':'100' , 'expected_result': {'test': 'lab1'      ,'datas':[]}},
            {'test':'lab1'      , 'score':'98'  , 'expected_result': {'test': 'lab1'      ,'datas':['ID: 975002069, Name: 練俊民, lab1\'s grade: 99','ID: 985002002, Name: 林芯妤, lab1\'s grade: 99','ID: 985002014, Name: 王祉鈞, lab1\'s grade: 99','ID: 985002027, Name: 張軒滄, lab1\'s grade: 99','ID: 985002028, Name: 許哲浩, lab1\'s grade: 99','ID: 985002036, Name: 陳健新, lab1\'s grade: 99','ID: 985002038, Name: 吳德毅, lab1\'s grade: 99','ID: 985002515, Name: 辜麟傑, lab1\'s grade: 98']}},
            {'test':'lab2'      , 'score':'100' , 'expected_result': {'test': 'lab2'      ,'datas':[]}},
            {'test':'lab1'      , 'score':'98.5', 'expected_result': {'test': 'lab1'      ,'datas':['ID: 975002069, Name: 練俊民, lab1\'s grade: 99','ID: 985002002, Name: 林芯妤, lab1\'s grade: 99','ID: 985002014, Name: 王祉鈞, lab1\'s grade: 99','ID: 985002027, Name: 張軒滄, lab1\'s grade: 99','ID: 985002028, Name: 許哲浩, lab1\'s grade: 99','ID: 985002036, Name: 陳健新, lab1\'s grade: 99','ID: 985002038, Name: 吳德毅, lab1\'s grade: 99']}},
            {'test':'lab3'      , 'score':'100' , 'expected_result': {'test': 'lab3'      ,'datas':[]}},
            {'test':'mid_term'  , 'score':'100' , 'expected_result': {'test': 'mid_term'  ,'datas':[]}},
            {'test':'final_exam', 'score':'100' , 'expected_result': {'test': 'final_exam','datas':[]}},
        ]
        
        for test_case in test_cases:
            test, score, expected_result = test_case.values()
            with self.subTest((test,score,expected_result)):
                mock_input.side_effect = [test,score]
                self.system.filtering()
                self.assertDictEqual(self.system.filter_student, expected_result)
                
    @patch('builtins.input')
    def test_invalid_input(self, mock_input):
        """
        Test description:
            Verifie the behavior of 'filtering' method with various invalid input formats.
        
        Test cases:
            Each test case includes test, and expected_result 
            representing  the test name (lab1, lab2 ...), and the correct filtered student data.

        Expected behavior:
            For each test case, result of 'filtering' method should match the expected result.
        """
        
        test_cases = [
            {'test':'!@#$%^&*()_.<>~'     , 'expected_result': {'test': '', 'datas':[]}},
            {'test':'sdsfwqeqfasfsgczxxcq', 'expected_result': {'test': '', 'datas':[]}},
            {'test':' '*50                , 'expected_result': {'test': '', 'datas':[]}},
            {'test':'\n\t\r'*50           , 'expected_result': {'test': '', 'datas':[]}},
        ]
        
        for test_case in test_cases:
            test, expected_result = test_case.values()
            with self.subTest((test,expected_result)):
                mock_input.side_effect = [test]
                self.system.filtering()
                self.assertDictEqual(self.system.filter_student, expected_result)