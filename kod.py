import os

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

def list_existing_lists():
    files = [f for f in os.listdir() if f.endswith('.txt')]
    lists = [os.path.splitext(f)[0] for f in files]
    return lists
#dodac_funkcjonalnosc

def main():
    while True:
        print("\nOpcje:")
        print("1. Dodaj nową listę")
        print("2. Zobacz istniejące listy")
        print("3. Usuń istniejącą listę")
        print("4. Wyjdź")
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

        elif choice == '2':
            lists = list_existing_lists()
            if lists:
                print("Twoje listy:")
                for i, tytul in enumerate(lists, 1):
                    print(f"{i}. {tytul}")
                list_choice = int(input("Wybierz numer listy lub 0 aby wrócić: "))
                if list_choice > 0 and list_choice <= len(lists):
                    list_manager = listy(lists[list_choice - 1])

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
            else:
                print("Nie znaleziono żadnych list.")

        elif choice == '3':
            lists = list_existing_lists()
            if lists:
                print("Twoje listy:")
                for i, tytul in enumerate(lists, 1):
                    print(f"{i}. {tytul}")
                list_choice = int(input("Wybierz numer listy do usunięcia lub 0 aby wrócić: "))
                if list_choice > 0 and list_choice <= len(lists):
                    list_manager = listy(lists[list_choice - 1])
                    list_manager.usun_liste()
            else:
                print("Nie znaleziono żadnych list.")

        elif choice == '4':
            break
        else:
            print("Błąd")

if __name__ == "__main__":
    main()
