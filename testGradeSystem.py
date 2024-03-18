import unittest
import sys
class DevNull:
    """
    Suppress print statements during test execution by redirecting stdout to an instance of DevNull, 
    which does nothing when written to.
    
    Attributes:
        None

    Methods:
        write(self, msg): A method that does nothing when called.
    """
    def write(self, msg):
        pass
    
def run_test(suite, disable_print=False):
    """
    Execute test cases.

    :param suite: unittest test suite.
    :type suite: unittest.TestSuite
    :return: None
    :rtype: None
    
    Running Example:
    >>>> run_test(suite)
    
    """
    # Save the current stdout
    old_stdout = sys.stdout
    
    if disable_print:
        sys.stdout = DevNull()

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    
    # Restore the original stdout
    sys.stdout = old_stdout

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
    Execute specific unit tests.
    """
    
    suite = set_suite()
    run_test(suite, disable_print=True)