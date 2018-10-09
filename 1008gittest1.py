import unittest
class TestGit1(unittest.TestCase):
    def __init__(self,name):
        unittest.TestCase.__init__(self,name)
        name = input("请输入你name：")
        self.name = name
    def test_01(self):
        self.assertEqual(self.name,"admin")
if __name__=="__main__":
    unittest.main()