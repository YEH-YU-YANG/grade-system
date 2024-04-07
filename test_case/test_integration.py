import unittest
from unittest.mock import patch
import sys 
sys.path.append("..") 
from gradeSystem import ScoreSystem


class TestIntegration(unittest.TestCase):
    """
    Test suite for the several method in the ScoreSystem class.
    
    Attributes:
        system : An instance of the ScoreSystem class initialized for testing.

    Methods:
        setUp: Initializes the ScoreSystem object and assigns it to self.system for use in test methods.
        tearDown: Cleans up the ScoreSystem object after each test.
        shortDescription: Prevent displaying test method descriptions.
        test_valid_input_1: Tests several method with various valid input.
        test_valid_input_2: Tests several method with various valid input.
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
    def test_valid_input_1(self, mock_input):
        """
        # TODO:
        """
    
    @patch('builtins.input')
    def test_valid_input_2(self, mock_input):
        """
        # TODO:
        """
    
