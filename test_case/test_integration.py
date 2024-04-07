import unittest
from unittest.mock import patch
import sys 
sys.path.append("..") 
from gradeSystem import ScoreSystem
from io import StringIO

class TestIntegration(unittest.TestCase):
    """
    Test suite for the several method in the ScoreSystem class.
    
    Attributes:
        system : An instance of the ScoreSystem class initialized for testing.

    Methods:
        setUp: Initializes the ScoreSystem object and assigns it to self.system for use in test methods.
        tearDown: Cleans up the ScoreSystem object after each test.
        shortDescription: Prevent displaying test method descriptions.
        test_integration_show_score
        test_integration_show_grade_letter
        test_integration_show_average
        test_integration_show_rank
        test_integration_show_distribution
        test_integration_filter
        test_integration_update_weight
    """
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
    def test_integration_show_score(self, mock_input):
        """
        Tests the integration of the system's input handling and score output.

        ensuring that the correct scores are provided as input and verifies that the system correctly
        outputs these scores.
        """
        inputs = [
            '8', '955002056', 'lab1 11 lab2 62 lab3 60 mid_term 60 final_exam 90',
            '1', '955002056',
            '10'
        ]

        expected_result = "Student's scores:\n" \
                            "+--------------+-------+\n" \
                            "|    Subject   | Score |\n" \
                            "+--------------+-------+\n" \
                            "|     Lab 1    |   11   |\n" \
                            "|     Lab 2    |   62   |\n" \
                            "|     Lab 3    |   60   |\n" \
                            "|   Mid-Term   |   60   |\n" \
                            "|  Final Exam  |   90   |\n" \
                            "+--------------+-------+"
                            
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            mock_input.side_effect = inputs
            self.system.run()
            
        captured_outputs = mock_output.getvalue().split('\n')
        captured_output = '\n'.join(captured_outputs[-26:-16])
        self.assertEqual(captured_output, expected_result)
        
    @patch('builtins.input')
    def test_integration_show_grade_letter(self, mock_input):
        """
        Tests the integration of the system's input handling and score output.

        ensuring that the correct scores are provided as input and verifies that the system correctly
        outputs grade letter.
        """
        inputs = [
            '8', '955002056', 'lab1 80 lab2 75 lab3 78 mid_term 20 final_exam 100',
            '2', '955002056',
            '10'
        ]

        expected_result = "Student's scores:  C+" 
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            mock_input.side_effect = inputs
            self.system.run()
            
        captured_outputs = mock_output.getvalue().split('\n')
        captured_output = captured_outputs[-17]
        self.assertEqual(captured_output, expected_result)
        
    @patch('builtins.input')
    def test_integration_show_average(self, mock_input):
        """
        Tests the integration of the system's input handling and score output.

        ensuring that the correct scores are provided as input and verifies that the system correctly
        outputs average scores.
        """
        inputs = [
            '8', '955002056', 'lab1 90 lab2 90 lab3 90 mid_term 90 final_exam 90',
            '3', '955002056',
            '10'
        ]

        expected_result = "Student's average scores: 90.00" 
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            mock_input.side_effect = inputs
            self.system.run()
            
        captured_outputs = mock_output.getvalue().split('\n')
        captured_output = captured_outputs[-17]
        self.assertEqual(captured_output, expected_result)
        
    @patch('builtins.input')
    def test_integration_show_rank(self, mock_input):
        """
        Tests the integration of the system's input handling and score output.

        ensuring that the correct scores are provided as input and verifies that the system correctly
        outputs rank.
        """
        inputs = [
            '8', '955002056', 'lab1 100 lab2 100 lab3 100 mid_term 100 final_exam 100',
            '4', '955002056',
            '10'
        ]
        
        expected_result = "Student's rank: 1" 
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            mock_input.side_effect = inputs
            self.system.run()
            

        captured_outputs = mock_output.getvalue().split('\n')
        captured_output = captured_outputs[-17]
        self.assertEqual(captured_output, expected_result)
            
    @patch('builtins.input')
    def test_integration_show_distribution(self, mock_input):
        """
        Tests the integration of the system's input handling and score output.

        ensuring that the correct scores are provided as input and verifies that the system correctly
        outputs distribution.
        """
        inputs = [
            '7', '12345', 'Ale', 'lab1 100 lab2 100 lab3 100 mid_term 100 final_exam 100',
            '5', 
            '10'
        ]
        
        expected_result = 'Grade distribution:\n' \
                            'A+: 28\n' \
                            'A : 33\n' \
                            'A-: 3'

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            mock_input.side_effect = inputs
            self.system.run()
            
        captured_outputs = mock_output.getvalue().split('\n')
        captured_output = '\n'.join(captured_outputs[-20:-16])
        self.assertEqual(captured_output, expected_result)
        
    @patch('builtins.input')
    def test_integration_filter(self, mock_input):
        """
        Tests the integration of the system's input handling and score output.

        ensuring that the student are correctly added as input and verifies that the system correctly
        outputs filter.
        """
        inputs = [
            '7', '12345', 'Ale', 'lab1 100 lab2 100 lab3 100 mid_term 100 final_exam 100',
            '8', '12345', 'lab1 99',
            '6', 'lab1', '99',
            '10'
        ]
        
        expected_result = {
            'test': 'lab1',
            'datas': [
                'ID: 975002069, Name: 練俊民, lab1\'s grade: 99',
                'ID: 985002002, Name: 林芯妤, lab1\'s grade: 99',
                'ID: 985002014, Name: 王祉鈞, lab1\'s grade: 99',
                'ID: 985002027, Name: 張軒滄, lab1\'s grade: 99',
                'ID: 985002028, Name: 許哲浩, lab1\'s grade: 99',
                'ID: 985002036, Name: 陳健新, lab1\'s grade: 99',
                'ID: 985002038, Name: 吳德毅, lab1\'s grade: 99',
                'ID: 12345, Name: Ale, lab1\'s grade: 99'
            ]
        }   

        mock_input.side_effect = inputs
        self.system.run()
        self.assertDictEqual(self.system.filter_student, expected_result)
        
        
    @patch('builtins.input')
    def test_integration_update_weight(self, mock_input):
        """
        Tests the integration of the system's input handling and score output.

        ensuring that the correct scores are provided as input, update weights correctly and verifies that the system correctly
        outputs grade letter.
        """
        inputs = [
            '8', '955002056', 'lab1 80 lab2 75 lab3 78 mid_term 20 final_exam 100',
            '9', 'lab1 0.2 lab2 0.2 lab3 0.2 mid_term 0.2 final_exam 0.2',
            '2', '955002056',
            '10'
        ]

        expected_result = "Student's scores:  B-" 
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            mock_input.side_effect = inputs
            self.system.run()
            
        captured_outputs = mock_output.getvalue().split('\n')
        captured_output = captured_outputs[-17]
        self.assertEqual(captured_output, expected_result)