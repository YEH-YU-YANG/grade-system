import unittest
from unittest.mock import patch
import sys 
from io import StringIO
sys.path.append("..") 
from gradeSystem import ScoreSystem

class TestShowDistribution(unittest.TestCase):
    """
    Test show_distribution function
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
    def test_show_Description(self, mock_input):
        """
        Test description:
            - Test shortDescription function
        Test case:
            - input.txt
        Expected output:
            - Grade distribution:
                A+: 27
                A : 33
                A-: 3
        """
        excepted_output = 'Grade distribution:\n' \
                            'A+: 27\n' \
                            'A : 33\n' \
                            'A-: 3\n'
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.system.show_distribution()
            self.assertEqual(mock_output.getvalue(), excepted_output)
        
# if __name__ == '__main__':
    
#     """
#     全部 Class 的 test case 一起測
#     """

#     unittest.main()