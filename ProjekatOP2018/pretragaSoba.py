import helpf
def pretragaSoba():
	print("Pretraga soba")
	print("1 - po broju sobe")
	print("2 - po broju kreveta")
	print("3 - po tipu ")
	print("4 - po klimi")
	print("5 - po tv-u")
	print("6 - po terasi")
	print("7 - po kupatilu")
	print("8 - po ceni")
	print("9 - po bilo kom kriterijumu")
	unos = input('>>>')
	print("-------------------")
	if unos == '1':
		soba = input("Unesite tacan broj sobe: ")
		otvori = open("soba.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[1] == soba:
				print(line)
		print("---------------------")
		otvori.close()
	elif unos == '2':
		krevet = input("Unesite tacan broj kreveta: ")
		otvori = open("soba.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[2] == krevet:
				print(line)
		print("---------------------")
		otvori.close()
	elif unos == '3':
		tip = input("Unesite tip sobe(apartman/soba): ")
		otvori = open("soba.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[3] == tip:
				print(line)
		print("----------------------")
		otvori.close()
	elif unos == '4':
		klima = input("Klima(da/ne): ")
		otvori = open("soba.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[4] == klima:
				print(line)
		print("---------------------")
		otvori.close()
	elif unos == '5':
		tv = input("TV(da/ne): ")
		otvori = open("soba.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[5] == tv:
				print(line)
		print("--------------------")
		otvori.close()
	elif unos == '6':
		terasa = input("Terasa(da/ne): ")
		otvori = open("soba.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[6] == terasa:
				print(line)
		print("--------------------")
		otvori.close()
	elif unos == '7':
		kupatilo = input("Kupatilo(da/ne): ")
		otvori = open("soba.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[7] == kupatilo:
				print(line)
		print("--------------------")
		otvori.close()
	elif unos == '8':
		cena = input("Unesite cenu po nocenju: ")
		otvori = open("soba.txt", "r")
		for line in otvori:
			line = line.split("|")
			if int(line[8]) == int(cena):
				print(line)
		print("----------------------")
		otvori.close()
	elif unos == '9':
		inf = input("Unesite informaciju: ")
		otvori = open("soba.txt", "r")
		for line in otvori:
			line = line.split("|")
			for i in line:
				if i == inf:
					print(helpf.listtostring(line))
		print("-----------------------")
		otvori.close()
	else: 
		print("Uneli ste nepostojecu opciju.")
pretragaSoba()
