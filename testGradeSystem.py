import unittest
from gradeSystem import ScoreSystem
    
def run_test(suite):
    """
    Execute test cases.

    :param suite: unittest test suite.
    :type suite: unittest.TestSuite
    :return: None
    :rtype: None
    
    Running Example:
        run_test(suite)
    
    """
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def set_suite():
    """
    Select the test files to be executed.
    
    :return: unittest test suite.
    :rtype: unittest.TestSuite
    
    Running Example:
        test_case_path = "./test_case/"
        test_case_pattern = "test_*.py"
        suite = set_suite()
        run_test(suite)
    """
    
    test_case_path = "./test_case/"
    test_case_pattern="test_*.py"

    suite = unittest.TestSuite()
    suite = unittest.TestLoader().discover(test_case_path,pattern=test_case_pattern)
    
    return suite


if __name__ == '__main__':
    
    """
    Run all tests together.
    """
    # unittest.main()
    
    """
    Run specific unit tests.
    If all test cases are in the same file.
    """
    
    # suit = unittest.TestSuite()
    # test_cases = [TestSubtract("test_1"), TestSubtract("test_2"), TestSubtract("test_3")]
    # suit.addTests(test_cases)

    # runner = unittest.TextTestRunner()
    # runner.run(suit)
    
    """
    Run specific unit tests.
    If test cases are split into multiple files.
    """
    
    suite = set_suite()
    run_test(suite)