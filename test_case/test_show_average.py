import unittest
from unittest.mock import patch
import sys 
sys.path.append("..") 
from gradeSystem import ScoreSystem

class TestShowAverage(unittest.TestCase):
    """
    Test show_average function
    """
    def setUp(self):
        """
        Method description:
            initializes the ScoreSystem object and assigns it to self.system so that it can be used in the test methods.
        """
        self.system = ScoreSystem()
    
    def shortDescription(self):
        """
        Method description:
            Override the shortDescription method to prevent displaying test method descriptions.
        """
        return None
        
        
# if __name__ == '__main__':
    
#     """
#     全部 Class 的 test case 一起測
#     """

#     unittest.main()