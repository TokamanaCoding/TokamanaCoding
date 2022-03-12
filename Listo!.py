#Ten program stworzył Mistersteve YT
#|- | | | -| Jest całkowitą własnością Mistersteve YT
#
#[C]Mistersteve YT wszystki prawa zastrzeżone
#[C]Mistersteve YT all rights reserved
a = "a"
todo = []

def aa():
	del_from_todo = input('Podaj co zrobiłeś a jeśli to pomyłka wpisz "fail"> ')
	if del_from_todo == "fail":
		start()
	else:
		todo.remove(del_from_todo)
		start()

def start():
	while a in a:
		add_to_todo = input("Dodaj Do Listy> ")
		todo.append(add_to_todo)
		print(todo)
		yn0 = input("Zrobiłeś coś? (Y/N)")
		if yn0 == "Y":
			aa()
		elif yn0 == "y":
			aa()
		elif yn0 == "n":
			start()
		elif yn0 == "N":
			start()
start()