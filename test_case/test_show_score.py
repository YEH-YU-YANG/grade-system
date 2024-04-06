import unittest
from unittest.mock import patch
import sys 
from io import StringIO
sys.path.append("..") 
from gradeSystem import ScoreSystem

class TestShowScore(unittest.TestCase):
    """
    Test show_score function
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
            self.system.show_score()
            self.assertEqual(mock_input.getvalue(), expected_output)
    
    
    @patch('builtins.input', side_effect=['985002006'])
    def test_valid_input(self, mock_input):
        """
        Test description:
            - Test show_score function
        
        Test case:
            - Input student id: 985002006
        
        Expected output:
            - Student's scores:
              +--------------+-------+
              |    Subject   | Score |
              +--------------+-------+
              |     Lab 1    |   82   |
              |     Lab 2    |   88   |
              |     Lab 3    |   85   |
              |   Mid-Term   |   89   |
              |  Final Exam  |   92   |
              +--------------+-------+
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            expected_output = "Student's scores:\n" \
                                "+--------------+-------+\n" \
                                "|    Subject   | Score |\n" \
                                "+--------------+-------+\n" \
                                "|     Lab 1    |   82   |\n" \
                                "|     Lab 2    |   88   |\n" \
                                "|     Lab 3    |   85   |\n" \
                                "|   Mid-Term   |   89   |\n" \
                                "|  Final Exam  |   92   |\n" \
                                "+--------------+-------+\n"
            self.system.show_score()
            self.assertEqual(mock_output.getvalue(), expected_output)
        
        
        
# if __name__ == '__main__':
    
#     """
#     全部 Class 的 test case 一起測
#     """

#     unittest.main()