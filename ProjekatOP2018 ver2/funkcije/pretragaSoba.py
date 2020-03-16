def formatSoba():
	print("Sifra |Br sobe|Br kreveta|Tip sobe|Klima|Tv|Ter.|Kup.|Cena")
	print("------+-------+----------+--------+-----+--+----+----+----")

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
		lista = []
		otvori = open("soba.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatSoba()
		for red in redovi:
			red = red.split("|")
			if red[1] == soba:
				recnik = {'sf':red[0],'bs':red[1],'bk':red[2],'t':red[3],'kl':red[4],'tv':red[5],'tr':red[6],'kp':red[7],'c':red[8]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:7}|{2:10}|{3:8}|{4:5}|{5:2}|{6:4}|{7:4}|{8:4}".format(i['sf'],i['bs'],i['bk'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c']))
		print("---------------------")
		otvori.close()
	elif unos == '2':
		krevet = input("Unesite tacan broj kreveta: ")
		lista = []
		otvori = open("soba.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatSoba()
		for red in redovi:
			red = red.split("|")
			if red[2] == krevet:
				recnik = {'sf':red[0],'bs':red[1],'bk':red[2],'t':red[3],'kl':red[4],'tv':red[5],'tr':red[6],'kp':red[7],'c':red[8]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:7}|{2:10}|{3:8}|{4:5}|{5:2}|{6:4}|{7:4}|{8:4}".format(i['sf'],i['bs'],i['bk'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c']))
		print("---------------------")
		otvori.close()
	elif unos == '3':
		tip = input("Unesite tip sobe(apartman/soba): ")
		lista = []
		otvori = open("soba.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatSoba()
		for red in redovi:
			red = red.split("|")
			if red[3] == tip:
				recnik = {'sf':red[0],'bs':red[1],'bk':red[2],'t':red[3],'kl':red[4],'tv':red[5],'tr':red[6],'kp':red[7],'c':red[8]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:7}|{2:10}|{3:8}|{4:5}|{5:2}|{6:4}|{7:4}|{8:4}".format(i['sf'],i['bs'],i['bk'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c']))
		print("----------------------")
		otvori.close()
	elif unos == '4':
		klima = input("Klima(da/ne): ")
		lista = []
		otvori = open("soba.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatSoba()
		for red in redovi:
			red = red.split("|")
			if red[4] == klima:
				recnik = {'sf':red[0],'bs':red[1],'bk':red[2],'t':red[3],'kl':red[4],'tv':red[5],'tr':red[6],'kp':red[7],'c':red[8]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:7}|{2:10}|{3:8}|{4:5}|{5:2}|{6:4}|{7:4}|{8:4}".format(i['sf'],i['bs'],i['bk'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c']))
		print("---------------------")
		otvori.close()
	elif unos == '5':
		tv = input("TV(da/ne): ")
		lista = []
		otvori = open("soba.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatSoba()
		for red in redovi:
			red = red.split("|")
			if red[5] == tv:
				recnik = {'sf':red[0],'bs':red[1],'bk':red[2],'t':red[3],'kl':red[4],'tv':red[5],'tr':red[6],'kp':red[7],'c':red[8]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:7}|{2:10}|{3:8}|{4:5}|{5:2}|{6:4}|{7:4}|{8:4}".format(i['sf'],i['bs'],i['bk'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c']))
		print("--------------------")
		otvori.close()
	elif unos == '6':
		terasa = input("Terasa(da/ne): ")
		lista = []
		otvori = open("soba.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatSoba()
		for red in redovi:
			red = red.split("|")
			if red[6] == terasa:
				recnik = {'sf':red[0],'bs':red[1],'bk':red[2],'t':red[3],'kl':red[4],'tv':red[5],'tr':red[6],'kp':red[7],'c':red[8]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:7}|{2:10}|{3:8}|{4:5}|{5:2}|{6:4}|{7:4}|{8:4}".format(i['sf'],i['bs'],i['bk'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c']))
		print("--------------------")
		otvori.close()
	elif unos == '7':
		kupatilo = input("Kupatilo(da/ne): ")
		lista = []
		otvori = open("soba.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatSoba()
		for red in redovi:
			red = red.split("|")
			if red[7] == kupatilo:
				recnik = {'sf':red[0],'bs':red[1],'bk':red[2],'t':red[3],'kl':red[4],'tv':red[5],'tr':red[6],'kp':red[7],'c':red[8]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:7}|{2:10}|{3:8}|{4:5}|{5:2}|{6:4}|{7:4}|{8:4}".format(i['sf'],i['bs'],i['bk'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c']))
		print("--------------------")
		otvori.close()
	elif unos == '8':
		cena = input("Unesite cenu po nocenju(opseg od 800 do 2000): ")
		lista = []
		otvori = open("soba.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatSoba()
		for red in redovi:
			red = red.split("|")
			if int(red[8]) <= int(cena) <= 2000:
				recnik = {'sf':red[0],'bs':red[1],'bk':red[2],'t':red[3],'kl':red[4],'tv':red[5],'tr':red[6],'kp':red[7],'c':red[8]}
				lista = [recnik]
				for i in lista:
					print("{0:6}|{1:7}|{2:10}|{3:8}|{4:5}|{5:2}|{6:4}|{7:4}|{8:4}".format(i['sf'],i['bs'],i['bk'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c']))
		print("----------------------")
		otvori.close()
	elif unos == '9':
		inf = input("Unesite informaciju: ")
		lista = []
		otvori = open("soba.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatSoba()
		for red in redovi:
			red = red.split("|")
			recnik = {'sf':red[0],'bs':red[1],'bk':red[2],'t':red[3],'kl':red[4],'tv':red[5],'tr':red[6],'kp':red[7],'c':red[8]}
			lista = [recnik]
			for i in red:
				if i == inf:
					for i in lista:
						print("{0:6}|{1:7}|{2:10}|{3:8}|{4:5}|{5:2}|{6:4}|{7:4}|{8:4}".format(i['sf'],i['bs'],i['bk'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c']))
		print("-----------------------")
		otvori.close()
	else: 
		print("Uneli ste nepostojecu opciju.")
pretragaSoba()