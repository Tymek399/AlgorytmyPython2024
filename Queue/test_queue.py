import unittest
from queue import Queue 

class TestQueue(unittest.TestCase):
    def test_queue_is_class(self):
        self.assertTrue(callable(getattr(Queue, '__init__')))

    def test_add_elements_to_queue(self):
        q = Queue()
        self.assertIsNotNone(q)
        q.add(1)
        self.assertEqual(q.queue, [1])

    def test_remove_elements_from_queue(self):
        q = Queue()
        q.add(1)
        self.assertEqual(q.remove(), 1)

    def test_order_of_elements_is_maintained(self):
        q = Queue()
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(q.remove(), 1)
        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)
        self.assertIsNone(q.remove())

if __name__ == '__main__':
    unittest.main()
