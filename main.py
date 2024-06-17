#od nowa
import os
import shutil

class listy:
    def __init__(self, tytul):
        self.tytul = tytul
        self.nazwa = f"{self.tytul}.txt"
        self.produkt = []
        self.wczytaj_produkt()

    def dodaj_produkt(self, produkt):
        self.produkt.append(produkt)
        with open(self.nazwa, 'a') as file:
            file.write(f"{produkt}\n")

    def wczytaj_produkt(self):
        if os.path.exists(self.nazwa):
            with open(self.nazwa, 'r') as file:
                self.produkt = file.readlines()
                self.produkt = [produkt.strip() for produkt in self.produkt]
        else:
            self.produkt = []
