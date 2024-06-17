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
    def wyswietl_produkt(self):
        self.wczytaj_produkt()
        if self.produkt:
            print(f"Produkty na liście '{self.tytul}':")
            for produkt in self.produkt:
                print(f"- {produkt}")
        else:
            print(f"Nie ma produktów na liście '{self.tytul}'.")

    def usun_liste(self):
        if os.path.exists(self.nazwa):
            os.remove(self.nazwa)
            print(f"Lista '{self.tytul}' została usunięta.")
        else:
            print(f"Lista '{self.tytul}' nie istnieje.")
    def zapisz_liste(self, sciezka):
        if os.path.exists(self.nazwa):
            shutil.copy(self.nazwa, sciezka)
            print(f"Lista '{self.tytul}' została zapisana pod ścieżką '{sciezka}'.")
        else:
            print(f"Lista '{self.tytul}' nie istnieje, więc nie można jej zapisać.")    

    def list_existing_lists():
        files = [f for f in os.listdir() if f.endswith('.txt')]
        lists = [os.path.splitext(f)[0] for f in files]
        return lists
def main():
    while True:
        print("\nOpcje:")
        print("1. Dodaj nową listę")
        print("2. Zobacz istniejące listy")
        print("3. Usuń istniejącą listę")
        print("4. Zapis pod ścieżką")
        print("5. Wyjdź")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            tytul = input("Tytuł nowej listy: ")
            list_manager = listy(tytul)

            while True:
                print("\nOpcje:")
                print("1. Dodaj produkt do listy")
                print("2. Wyświetl produkty z tej listy")
                print("3. Wróć")
                sub_choice = input("Wybierz opcję: ")

                if sub_choice == '1':
                    produkt = input("Wprowadź produkt: ")
                    list_manager.dodaj_produkt(produkt)
                elif sub_choice == '2':
                    list_manager.wyswietl_produkt()
                elif sub_choice == '3':
                    break
                else:
                    print("Błąd")
