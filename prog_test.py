import unittest
from prog import getTitle
class TestTex(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_url(self):
        self.assertEqual( getTitle('http://nedbatchelder.com/code/coverage'), 'Ned Batchelder: coverage.py')

if __name__ == '__main__':
    unittest.main()