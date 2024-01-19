import unittest
from test_queue import TestQueue

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueue)
    unittest.TextTestRunner(verbosity=2).run(suite)
