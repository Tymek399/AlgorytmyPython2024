 from collections import deque

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
