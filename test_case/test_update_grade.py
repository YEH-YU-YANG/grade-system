import unittest
from gradeSystem import ScoreSystem


class TestUpdateGrade(unittest.TestCase):
    """
    Test update_grade function
    """
    def setUp(self):
        # 在每個測試方法執行前設置所需的資源
        self.system = ScoreSystem()
        
        
# if __name__ == '__main__':
    
#     """
#     全部 Class 的 test case 一起測
#     """

#     unittest.main()