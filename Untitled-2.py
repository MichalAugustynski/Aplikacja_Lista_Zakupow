class ListManager:
    def __init__(self):
        self.lists = {}

    def add_list(self):
        list_name = input("Podaj nazwę nowej listy: ")
        if list_name in self.lists:
            print("Lista o tej nazwie już istnieje.")
        else:
            self.lists[list_name] = []
            print(f"Lista '{list_name}' została dodana.")

    def add_products_to_list(self):
        list_name = input("Podaj nazwę listy, do której chcesz dodać produkty: ")
        if list_name not in self.lists:
            print("Lista o podanej nazwie nie istnieje.")
            return

        while True:
            product = input(f"Dodaj produkt do listy '{list_name}' (lub wpisz 'q' aby zakończyć): ")
            if product.lower() == 'q':
                break
            self.lists[list_name].append(product)
            print(f"Produkt '{product}' został dodany do listy '{list_name}'.")

    def view_lists(self):
        if not self.lists:
            print("Brak istniejących list.")
        else:
            print("Istniejące listy:")
            for list_name, products in self.lists.items():
                print(f"- {list_name}: {', '.join(products) if products else 'Brak produktów'}")

    def delete_list(self):
        list_name = input("Podaj nazwę listy do usunięcia: ")
        if list_name in self.lists:
            del self.lists[list_name]
            print(f"Lista '{list_name}' została usunięta.")
        else:
            print("Lista o podanej nazwie nie istnieje.")

    def display_menu(self):
        print("\nOpcje:")
        print("1. Dodaj nową listę")
        print("2. Dodaj produkty do listy")
        print("3. Zobacz istniejące listy")
        print("4. Usuń istniejącą listę")
        print("5. Wyjdź")

    def run(self):
        while True:
            self.display_menu()
            option = input("Wybierz opcję: ")
            if option == '1':
                self.add_list()
            elif option == '2':
                self.add_products_to_list()
            elif option == '3':
                self.view_lists()
            elif option == '4':
                self.delete_list()
            elif option == '5':
                print("Do widzenia!")
                break
            else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

 main():if
    manager = ListManager()
    manager.run()
