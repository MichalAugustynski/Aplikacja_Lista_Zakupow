import os

def title_of_list():
    title_list = input("Give the name the list of items: ")

    folder_path = './lists'  # Możesz zmienić ścieżkę do folderu, gdzie będą przechowywane listy
    file_path = os.path.join(folder_path, f"{title_list}.txt")

    # 3. Umożliwienie użytkownikowi dodawania przedmiotów do listy i zapisywanie ich do pliku
    print(f"Creating new lists: {title_list}")
    print("to finish write 'end'.")

    with open(file_path, 'w') as file:
        file.write(f"Lista zakupów: {title_list}\n")
        file.write("-----------------\n")

        while True:
            item = input("Dodaj przedmiot do listy zakupów: ")
            if item.lower() == 'end':
                break
            file.write(f"- {item}\n")

    print(f"Lista zakupów '{title_list}' została zapisana do pliku: {file_path}")


title_of_list()
def edit_list():




