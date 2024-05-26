import os
def create_new_list(folder_path,name, length,title):
	file_path = os.path.join(folder_path,name)
	with open(file_path,'w') as file:
		str_punctation = title + "\n" + "---------------------" + "\n"

		for i in range(1,length+1):
			str_ = f'{i}. \n'
			str_punctation += str_
			# file.write(i,'.')
		file.write(str_punctation)

title = input("Tytuł listy: ")
folder_path = r"C:\Users\gracz\Desktop"
file_name = input("Nazwa listy: ") + ".txt"
length =int(input("Jak długa ma byc twoja lista?"))
create_new_list(folder_path,file_name,length,title)

