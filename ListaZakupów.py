class ListaZakupow:
    def __init__(self, tytul):
        self.tytul = tytul
        self.produkty = []

    def dodaj_produkt(self, dlugosc):
        for i in range(1, dlugosc + 1):
            produkt = input(f"Podaj ilość produktów: ")
            self.items.append(produkt)

    def save_to_file(self, sciezka_pliku, nazwa_pliku):
        file_path = os.path.join(sciezka_pliku, nazwa_pliku)
        try:
            with open(file_path, 'w') as file:
                file.write(self.__str__())
            print("Ścieżka twojej listy: ", file_path)
        except Exception as e:
            print(f"Błąd podczas zapisywania pliku: {e}")

    def __str__(self):
        str_punctation = self.title + "\n"
        for i, produkt in enumerate(self.produkt, start=1):
            str_punctation += f"{i}. {produkt}\n"
        return str_punctation