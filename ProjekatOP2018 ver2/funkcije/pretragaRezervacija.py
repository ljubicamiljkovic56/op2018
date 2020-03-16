def formatTabela():
	print("Sifra |Sb|Datum rezervac. |Datum prijave   |Datum odjave    |K.ime |Tip sobe|Kl|Tv|Kp|Tr|Cena|Rezerv.|O")
	print("------+--+----------------+----------------+----------------+------+--------+--+--+--+--+----+-------+-")

def pretragaRezervacija():
	print("Pretraga rezervacija")
	print("1 - Pretraga po korisniku")
	print("2 - Pretraga po bilo kom kriterijumu")
	unos = input(">>>")
	print("--------------------")
	if unos == '1':
		korisnik = input("Unesite tacno korisnicko ime korisnika: ")
		lista = []
		otvori = open("rezervacija.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatTabela()
		for red in redovi:
			red = red.split("|")
			if red[5] == korisnik:
				recnik = {'sf':red[0],'sb':red[1],'dr':red[2],'dp':red[3],'do':red[4],'k':red[5],'t':red[6],'kl':red[7],'tv':red[8],'tr':red[9],'kp':red[10],'c':red[11],'r':red[12],'o':red[13]}
				lista = [recnik]
				for i in lista:
					print("{0:2}|{1:2}|{2:4}|{3:4}|{4:4}|{5:4}|{6:4}|{7:2}|{8:2}|{9:2}|{10:2}|{11:3}|{12:3}|{13:1}".format(i['sf'],i['sb'],i['dr'],i['dp'],i['do'],i['k'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c'],i['r'],i['o']))
		print("--------------------")
		otvori.close()
	elif unos == '2':
		inf = input("Unesite informaciju: ")
		lista = []
		otvori = open("rezervacija.txt", "r")
		redovi = otvori.readlines()
		recnik = {}
		formatTabela()
		for red in redovi:
			red = red.split("|")
			recnik = {'sf':red[0],'sb':red[1],'dr':red[2],'dp':red[3],'do':red[4],'k':red[5],'t':red[6],'kl':red[7],'tv':red[8],'tr':red[9],'kp':red[10],'c':red[11],'r':red[12],'o':red[13]}
			lista = [recnik]
			for i in red:
				if i == inf:
					for i in lista:
						print("{0:2}|{1:2}|{2:4}|{3:4}|{4:4}|{5:4}|{6:4}|{7:2}|{8:2}|{9:2}|{10:2}|{11:3}|{12:3}|{13:1}".format(i['sf'],i['sb'],i['dr'],i['dp'],i['do'],i['k'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c'],i['r'],i['o']))
		print("-----------------------")
		otvori.close()
	else:
		print("Uneli ste nepostojecu opciju.")


pretragaRezervacija()