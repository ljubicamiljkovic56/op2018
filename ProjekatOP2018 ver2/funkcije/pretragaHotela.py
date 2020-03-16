def formatTabela():
	print("Sifra |Naziv     |Adresa    |Soba |Bazen|Rest.|Cena |Ocena")
	print("------+----------+----------+-----+-----+-----+-----+------")

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
		lista = []
		otvori = open("hotel.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatTabela()
		for red in redovi:
			red = red.split("|")
			if red[1] == naziv:
				recnik = {'sf':red[0],'n':red[1],'ad':red[2],'sb':red[3],'b':red[4],'r':red[5],'c':red[6],'o':red[7]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:10}|{2:10}|{3:5}|{4:5}|{5:5}|{6:5}|{7:1}".format(i['sf'],i['n'],i['ad'],i['sb'],i['b'],i['r'],i['c'],i['o']))
		print("---------------------")
		otvori.close()
	elif unos == '2':
		adresa = input("Unesite tacnu adresu hotela: ")
		lista = []
		otvori = open("hotel.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatTabela()
		for red in redovi:
			red = red.split("|")
			if red[2] == adresa:
				recnik = {'sf':red[0],'n':red[1],'ad':red[2],'sb':red[3],'b':red[4],'r':red[5],'c':red[6],'o':red[7]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:10}|{2:10}|{3:5}|{4:5}|{5:5}|{6:5}|{7:1}".format(i['sf'],i['n'],i['ad'],i['sb'],i['b'],i['r'],i['c'],i['o']))
		print("---------------------")
		otvori.close()
	elif unos == '3':
		ocena = input("Unesite tacnu ocenu hotela: ")
		lista = []
		otvori = open("hotel.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatTabela()
		for red in redovi:
			red = red.split("|")
			if red[7] == ocena:
				recnik = {'sf':red[0],'n':red[1],'ad':red[2],'sb':red[3],'b':red[4],'r':red[5],'c':red[6],'o':red[7]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:10}|{2:10}|{3:5}|{4:5}|{5:5}|{6:5}|{7:1}".format(i['sf'],i['n'],i['ad'],i['sb'],i['b'],i['r'],i['c'],i['o']))
		print("---------------------")
		otvori.close()
	elif unos == '4':
		inf = input("Unesite informaciju: ")
		lista = []
		otvori = open("hotel.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatTabela()
		for red in redovi:
			red = red.split("|")
			recnik = {'sf':red[0],'n':red[1],'ad':red[2],'sb':red[3],'b':red[4],'r':red[5],'c':red[6],'o':red[7]}
			lista = [recnik]
			for i in red:
				if i == inf:
					for i in lista:
						print("{0:6}|{1:10}|{2:10}|{3:5}|{4:5}|{5:5}|{6:5}|{7:1}".format(i['sf'],i['n'],i['ad'],i['sb'],i['b'],i['r'],i['c'],i['o']))
		print("-----------------------")
		otvori.close()
	else:
		print("Uneli ste nepostojecu opciju.")
pretragaHotela()