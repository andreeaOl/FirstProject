import unittest
from prog import getTitle
class TestProg(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_lowercase(self):
        self.assertEqual( getTitle('http://nedbatchelder.com/code/coverage'), 'Ned Batchelder: coverage.py')
    def test_uppercase(self):
        self.assertEqual(getTitle('http://www.cse.chalmers.se/edu/year/2013/course/TDA452/'), 'Functional Programming 2013, TDA 452, DIT 142')
if __name__ == '__main__':
    unittest.main()