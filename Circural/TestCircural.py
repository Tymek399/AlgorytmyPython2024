
import unittest
from circular import ListaPolaczona, Lista, cykliczna

class TestCircularDetection(unittest.TestCase):
    def test_cyliczna_is_function(self):
        self.assertTrue(callable(cykliczna))

    def test_cyliczna_detects_circular_linked_lists(self):
        l = ListaPolaczona()
        a = Lista('a')
        b = Lista('b')
        c = Lista('c')

        l.glowa = a
        a.nastepny = b
        b.nastepny = c
        c.nastepny = b

        result = cykliczna(l)
        self.assertTrue(result)

    def test_cyliczna_detects_circular_linked_lists_linked_at_the_head(self):
        l = ListaPolaczona()
        a = Lista('a')
        b = Lista('b')
        c = Lista('c')

        l.glowa = a
        a.nastepny = b
        b.nastepny = c
        c.nastepny = a

        result = cykliczna(l)
        self.assertTrue(result)

    def test_cyliczna_detects_non_circular_linked_lists(self):
        l = ListaPolaczona()
        a = Lista('a')
        b = Lista('b')
        c = Lista('c')

        l.glowa = a
        a.nastepny = b
        b.nastepny = c
        c.nastepny = None

        result = cykliczna(l)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
