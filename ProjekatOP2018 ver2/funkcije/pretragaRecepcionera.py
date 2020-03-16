def formatRecepcioner():
	print("K.ime |Lozinka |Ime     |Prezime |Broj tel.|Email          |Uloga|Sifra hotela")
	print("------+--------+--------+--------+---------+---------------+-----+------------")

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
		lista = []
		otvori = open("recepcioner.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatRecepcioner()
		for red in redovi:
			red = red.split("|")
			if red[2] == ime:
				recnik = {'k':red[0],'l':red[1],'i':red[2],'p':red[3],'bt':red[4],'e':red[5],'u':red[6],'sh':red[7]}
				lista = [recnik]
				for i in lista:
					print("{0:5}|{1:8}|{2:8}|{3:8}|{4:9}|{5:10}|{6:5}|{7:6}".format(i['k'],i['l'],i['i'],i['p'],i['bt'],i['e'],i['u'],i['sh']))
		print("---------------------")
		otvori.close()
	elif unos == '2':
		prezime = input("Unesite prezime recepcionera: ")
		lista = []
		otvori = open("recepcioner.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatRecepcioner()
		for red in redovi:
			red = red.split("|")
			if red[3] == prezime:
				recnik = {'k':red[0],'l':red[1],'i':red[2],'p':red[3],'bt':red[4],'e':red[5],'u':red[6],'sh':red[7]}
				lista = [recnik]
				for i in lista:
					print("{0:5}|{1:8}|{2:8}|{3:8}|{4:9}|{5:10}|{6:5}|{7:6}".format(i['k'],i['l'],i['i'],i['p'],i['bt'],i['e'],i['u'],i['sh']))
		print("---------------------")
		otvori.close()
	elif unos == '3':
		email = input("Unesite email recepcionera: ")
		lista = []
		otvori = open("recepcioner.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatRecepcioner()
		for red in redovi:
			red = red.split("|")
			if red[5] == email:
				recnik = {'k':red[0],'l':red[1],'i':red[2],'p':red[3],'bt':red[4],'e':red[5],'u':red[6],'sh':red[7]}
				lista = [recnik]
				for i in lista:
					print("{0:5}|{1:8}|{2:8}|{3:8}|{4:9}|{5:10}|{6:5}|{7:6}".format(i['k'],i['l'],i['i'],i['p'],i['bt'],i['e'],i['u'],i['sh']))
		print("----------------------")
		otvori.close()
	elif unos == '4':
		k_ime = input("Unesite korisnicko ime recepcionera: ")
		lista = []
		otvori = open("recepcioner.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatRecepcioner()
		for red in redovi:
			red = red.split("|")
			if red[0] == k_ime:
				recnik = {'k':red[0],'l':red[1],'i':red[2],'p':red[3],'bt':red[4],'e':red[5],'u':red[6],'sh':red[7]}
				lista = [recnik]
				for i in lista:
					print("{0:5}|{1:8}|{2:8}|{3:8}|{4:9}|{5:10}|{6:5}|{7:6}".format(i['k'],i['l'],i['i'],i['p'],i['bt'],i['e'],i['u'],i['sh']))
		print("----------------------")
		otvori.close()
	elif unos == '5':
		sifra = input("Unesite sifru hotela u kome recepcioner radi: ")
		lista = []
		otvori = open("recepcioner.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatRecepcioner()
		for red in redovi:
			red = red.split("|")
			if red[7] == sifra:
				recnik = {'k':red[0],'l':red[1],'i':red[2],'p':red[3],'bt':red[4],'e':red[5],'u':red[6],'sh':red[7]}
				lista = [recnik]
				for i in lista:
					print("{0:5}|{1:8}|{2:8}|{3:8}|{4:9}|{5:10}|{6:5}|{7:6}".format(i['k'],i['l'],i['i'],i['p'],i['bt'],i['e'],i['u'],i['sh']))
		print("----------------------")
		otvori.close()
	elif unos == '6':
		inf = input("Unesite informaciju: ")
		lista = []
		otvori = open("recepcioner.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatRecepcioner()
		for red in redovi:
			red = red.split("|")
			recnik = {'k':red[0],'l':red[1],'i':red[2],'p':red[3],'bt':red[4],'e':red[5],'u':red[6],'sh':red[7]}
			lista = [recnik]
			for i in red:
				if i == inf:
					for i in lista:
						print("{0:5}|{1:8}|{2:8}|{3:8}|{4:9}|{5:10}|{6:5}|{7:6}".format(i['k'],i['l'],i['i'],i['p'],i['bt'],i['e'],i['u'],i['sh']))
		print("-----------------------")
		otvori.close()
	else:
		print("Uneli ste nepostojecu opciju.")

pretragaRecepcionera()