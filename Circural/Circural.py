class Lista:

    def __init__(self, data):
        self.data = data
        self.nastepny = None

class ListaPolaczona:
    def __init__(self):
        self.glowa = None

def cykliczna(lista):
    if not lista.glowa:
        return False

    wolny = lista.glowa
    szybki = lista.glowa


    while szybki and szybki.nastepny:
        wolny = wolny.nastepny
        szybki = szybki.nastepny.nastepny

        if wolny == szybki:
            return True
    return False
