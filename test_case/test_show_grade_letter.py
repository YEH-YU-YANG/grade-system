import unittest
from unittest.mock import patch
import sys 
from io import StringIO
sys.path.append("..") 
from gradeSystem import ScoreSystem

class TestShowGradeLetter(unittest.TestCase):
    """
    Test show_grade_letter function
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
    
    @patch('builtins.input', side_effect=['985006\n'])
    def test_invalid_student_id(self, mock_input):
        """
        Test description:
            - Test show_score function with invalid student id
            
        Test case:
            - Input student id: 985006
        
        Expected output:
            - Student ID not found.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_input:
            expected_output = "Student ID not found.\n"
            self.system.show_grade_letter()
            self.assertEqual(mock_input.getvalue(), expected_output)
    
    @patch('builtins.input', side_effect=['985002006'])
    def test_valid_input(self, mock_input):
        """
        Test description:
            - Test show_score function
        
        Test case:
            - Input student id: 985002006
        
        Expected output:
            - Student's scores:  A
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_input:
            expected_output = "Student's scores:  A \n"
            self.system.show_grade_letter()
            self.assertEqual(mock_input.getvalue(), expected_output)
            
# if __name__ == '__main__':
    
#     """
#     全部 Class 的 test case 一起測
#     """

#     unittest.main()