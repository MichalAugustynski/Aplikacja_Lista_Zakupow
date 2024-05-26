import Groceries_list

title = input("Tytuł listy: ")
folder_path = r"C:\Users 
# Powyżej trzeba dodac ścieżkę na razie zostawiłem to tak

file_name = input("Nazwa listy: ") + ".txt"
length =int(input("Jak długa ma byc twoja lista?"))
Groceries_list.create_new_list(folder_path,file_name,length,title)