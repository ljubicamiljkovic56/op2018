import helpf
def pretragaRecepcionera():
	print("Pretraga recepcionera")
	print("1 - po imenu")
	print("2 - po prezimenu")
	print("3 - po email-u")
	print("4 - po korisnickom imenu")
	print("5 - po sifri hotela")
	print("6 - po bilo kom kriterijumu")
	unos = input(">>>")
	print("--------------------")
	if unos == '1':
		ime = input("Unesite ime recepcionera: ")
		otvori = open("recepcioner.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[2] == ime:
				print(helpf.listtostring(line))
		print("---------------------")
		otvori.close()
	elif unos == '2':
		prezime = input("Unesite prezime recepcionera: ")
		otvori = open("recepcioner.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[3] == prezime:
				print(helpf.listtostring(line))
		print("---------------------")
		otvori.close()
	elif unos == '3':
		email = input("Unesite email recepcionera: ")
		otvori = open("recepcioner.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[5] == email:
				print(helpf.listtostring(line))
		print("----------------------")
		otvori.close()
	elif unos == '4':
		k_ime = input("Unesite korisnicko ime recepcionera: ")
		otvori = open("recepcioner.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[0] == k_ime:
				print(helpf.listtostring(line))
		print("----------------------")
		otvori.close()
	elif unos == '5':
		sifra = input("Unesite sifru hotela u kome recepcioner radi: ")
		otvori = open("recepcioner.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[7] == sifra:
				print(helpf.listtostring(line))
		print("----------------------")
		otvori.close()
	elif unos == '6':
		inf = input("Unesite informaciju: ")
		otvori = open("recepcioner.txt", "r")
		for line in otvori:
			line = line.split("|")
			for i in line:
				if i == inf:
					print(helpf.listtostring(line))
		print("-----------------------")
		otvori.close()
	else:
		print("Uneli ste nepostojecu opciju.")
pretragaRecepcionera()