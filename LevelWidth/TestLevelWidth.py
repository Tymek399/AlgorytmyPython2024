from collections import deque
import unittest

class Wezel:
    def __init__(self, dane):
        self.dane = dane
        self.dzieci = []

def szerokosc_poziomow(korzen):
    if not korzen:
        return []

    wynik = []
    kolejka = deque([korzen])

    while kolejka:
        rozmiar_poziomu = len(kolejka)
        wynik.append(rozmiar_poziomu)

        for _ in range(rozmiar_poziomu):
            biezacy = kolejka.popleft()
            kolejka.extend(biezacy.dzieci)

    return wynik

class TestSzerokoscPoziomow(unittest.TestCase):
    def test_level_width_is_function(self):
        # Assuming you have levelWidth function in a separate file
        from index import szerokosc_poziomow as levelWidth
        self.assertTrue(callable(levelWidth))

    def test_level_width_returns_number_of_nodes_at_widest_point_1(self):
        root = Wezel(0)
        root.dzieci = [Wezel(1), Wezel(2), Wezel(3)]
        root.dzieci[0].dzieci = [Wezel(4)]
        root.dzieci[2].dzieci = [Wezel(5)]

        result = szerokosc_poziomow(root)
        self.assertEqual(result, [1, 3, 2])

    def test_level_width_returns_number_of_nodes_at_widest_point_2(self):
        root = Wezel(0)
        root.dzieci = [Wezel(1)]
        root.dzieci[0].dzieci = [Wezel(2), Wezel(3)]
        root.dzieci[0].dzieci[0].dzieci = [Wezel(4)]

        result = szerokosc_poziomow(root)
        self.assertEqual(result, [1, 1, 2, 1])

if __name__ == '__main__':
    unittest.main()
