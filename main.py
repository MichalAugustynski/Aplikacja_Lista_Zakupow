import Groceries_list


title = input("Tytuł listy: ")
# folder_path = r"C:\Users
# Powyżej trzeba dodac ścieżkę na razie zostawiłem to tak
folder_path_name = input("Podaj ścieżkę, w której chcesz zapisać swoją listę: ")
file_name = input("Nazwa listy: ") + ".txt"
length =int(input("Jak długa ma byc twoja lista?"))
Groceries_list.create_new_list(folder_path_name,file_name,length,title)