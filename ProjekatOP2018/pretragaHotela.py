import helpf
def pretragaHotela():
	print("Pretraga hotela")
	print("1 - po nazivu")
	print("2 - po adresi")
	print("3 - po oceni")
	print("4 - po bilo kom kriterijumu")
	unos = input(">>>")
	print("--------------------")
	if unos == '1':
		naziv = input("Unesite tacan naziv hotela: ")
		otvori = open("hotel.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[1] == naziv:
				print(line)
		print("---------------------")
		otvori.close()
	elif unos == '2':
		adresa = input("Unesite tacnu adresu hotela: ")
		otvori = open("hotel.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[2] == adresa:
				print(line)
		print("---------------------")
		otvori.close()
	elif unos == '3':
		ocena = input("Unesite tacnu ocenu hotela: ")
		otvori = open("hotel.txt", "r")
		for line in otvori:
			line = line.split("|")
			if int(line[7]) == int(ocena):
				print(line)
		print("---------------------")
		otvori.close()
	elif unos == '4':
		inf = input("Unesite informaciju: ")
		otvori = open("hotel.txt", "r")
		for line in otvori:
			line = line.split("|")
			for i in line:
				if i == inf:
					print(helpf.listtostring(line))
		print("-----------------------")
		otvori.close()
	else:
		print("Uneli ste nepostojecu opciju.")

pretragaHotela()
