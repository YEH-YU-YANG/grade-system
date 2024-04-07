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

    :param suite: A unittest test suite containing the test cases to be executed.
    :type suite: unittest.TestSuite
    
    :param disable_print: A boolean flag indicating whether to suppress print outputs during test execution. Default is False.
    :type disable_print: bool
    
    :return: None
    :rtype: None

    Example:
    >>> run_test(suite)
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
    Construct a unittest test suite.

    This function searches for test files matching a specific pattern in the specified directory and constructs a test suite from them.

    :return: A unittest test suite containing the test cases discovered from the test files.
    :rtype: unittest.TestSuite
    
    Running Example:
    >>> set_suite()
    # return a unittest.TestSuite with spectif pattern
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