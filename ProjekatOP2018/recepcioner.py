import helpf
def main():
	naslov()
	while True:
		recepcioner_meni()
		opcija = input('>>>')
		if opcija == '1':
			rezervacija()
		elif opcija == '2':
			pretragaSoba()
		elif opcija == '3':
			pretragaRezervacija()
		elif opcija == '4':
			izvestaj()
		elif opcija == '5':
			odjava()
		else: 
			print("Opcija nije prepoznata.")

def naslov():
	print("Hotel Servis")
	print("-------------")

def recepcioner_meni():
	print("1. Rezervacija")
	print("2. Pretraga soba")
	print("3. Pretraga rezervacija")
	print("4. Izvestaj")
	print("5. Odjava")

def rezervacija():
	print("Rezervacija")
	otvori = open("rezervacija.txt", "a")
	sifra = input("Unesite sifru hotela(6 cifara):  ")
	soba = input("Unesite broj sobe/soba: ")
	dat1 = input("Datum i vreme rezervacije(yyyy-mm-dd hh:mm): ")
	dat2 = input("Datum prijave(yyyy-mm-dd hh:mm): ")
	dat3 = input("Datum odjave(yyyy-mm-dd hh:mm): ")
	korisnik = input("Unesite korisnicko ime korisnika: ")
	tip = input("Unesite tip sobe(apartman/soba): ")
	klima = input("Klima(da/ne): ")
	tv = input("TV(da/ne): ")
	terasa = input("Terasa(da/ne): ")
	kupatilo = input("Kupatilo, deljeno ili ne(da/ne): ")
	cena = input("Cena po nocenju: ")
	rez = input("Rezervacija (nije zapoceta, u toku, zavrsena): ")
	ocena = input("Ocenite hotel(1-5): ")
	otvori = open("rezervacija.txt", "a")
	otvori.write(sifra + "|" + soba + "|" + dat1 + "|" + dat2 + "|" + dat3 + "|" + korisnik + "|" + tip + "|" + klima + "|" + tv + "|" + terasa + "|" + kupatilo + "|" + cena + "|" + rez + "|" + ocena + "\n")
	otvori.close()
	print("Uspesna rezervacija") 

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


def izvestaj():
	print("1. Lista realizovanih rezervacija")
	print("2. Ukupan broj realizovanih rezervacija")
	print("3. Ukupan broj izdatih soba")
	print("4. Ukupna zarada za dati period")
	print("5. Prosecna ocena za dati period")
	print("6. Nazad")
	opcija = input("Unesite zeljenu opciju: ")
	if opcija == '1':
		formatRez()
		listaRez()
	elif opcija == '2':
		formatRez()
		brojRez()
	elif opcija == '3':
		formatRez()
		brojSoba()
	elif opcija == '4':
		zarada()
	elif opcija == '5':
		formatRez()
		prosecnaOcena()
	elif opcija == '6':
		return 
	else:
		print("Nepostojeca opcija")

def formatRez():
	print("Sifra |Sb|Datum rezervac. |Datum prijave   |Datum odjave    |K.ime |Tip sobe|Kl|Tv|Kp|Tr|Cena|Rezerv.|O")
	print("------+--+----------------+----------------+----------------+------+--------+--+--+--+--+----+-------+-")
def listaRez():
	lista = []
	fajl = open("rezervacija.txt","r")
	redovi = fajl.readlines()
	fajl.close()
	recnik = {}
	for red in redovi:
		red = red.split("|")
		if red[12] == 'zavrsen':
			recnik = {'sf':red[0],'sb':red[1],'dr':red[2],'dp':red[3],'do':red[4],'k':red[5],'t':red[6],'kl':red[7],'tv':red[8],'tr':red[9],'kp':red[10],'c':red[11],'r':red[12],'o':red[13]}
			lista = [recnik]
			for i in lista:
				print("{0:2}|{1:2}|{2:4}|{3:4}|{4:4}|{5:4}|{6:4}|{7:2}|{8:2}|{9:2}|{10:2}|{11:3}|{12:3}|{13:1}".format(i['sf'],i['sb'],i['dr'],i['dp'],i['do'],i['k'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c'],i['r'],i['o']))

def brojRez():
	lista = []
	fajl = open("rezervacija.txt","r")
	redovi = fajl.readlines()
	fajl.close()
	recnik = {}
	broj = 0
	for red in redovi:
		red = red.split("|")
		if red[12] == 'zavrsen':
			recnik = {'sf':red[0],'sb':red[1],'dr':red[2],'dp':red[3],'do':red[4],'k':red[5],'t':red[6],'kl':red[7],'tv':red[8],'tr':red[9],'kp':red[10],'c':red[11],'r':red[12],'o':red[13]}
			lista = [recnik]
			broj = broj + 1
			for i in lista:
				print("{0:2}|{1:2}|{2:4}|{3:4}|{4:4}|{5:4}|{6:4}|{7:2}|{8:2}|{9:2}|{10:2}|{11:3}|{12:3}|{13:1}".format(i['sf'],i['sb'],i['dr'],i['dp'],i['do'],i['k'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c'],i['r'],i['o']))
	print("Ukupno realizovanih rezervacija: ", broj)

def brojSoba():
	lista = []
	fajl = open("rezervacija.txt","r")
	redovi = fajl.readlines()
	fajl.close()
	recnik = {}
	broj = 0
	for red in redovi:
		red = red.split("|")
		if red[1] != 0:
			recnik = {'sf':red[0],'sb':red[1],'dr':red[2],'dp':red[3],'do':red[4],'k':red[5],'t':red[6],'kl':red[7],'tv':red[8],'tr':red[9],'kp':red[10],'c':red[11],'r':red[12],'o':red[13]}
			lista = [recnik]
			broj = broj + 1
			for i in lista:
				print("{0:2}|{1:2}|{2:4}|{3:4}|{4:4}|{5:4}|{6:4}|{7:2}|{8:2}|{9:2}|{10:2}|{11:3}|{12:3}|{13:1}".format(i['sf'],i['sb'],i['dr'],i['dp'],i['do'],i['k'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c'],i['r'],i['o']))
	print("Ukupno izdatih soba: ", broj)

def zarada():
	datum = input("Unesite datum: ")
	otvori = open("rezervacija.txt", "r")
	redovi = otvori.readlines()
	otvori.close()
	recnik = {}
	broj = 0
	formatRez()
	for red in redovi:
		red = red.split("|")
		if red[2] == datum:
			recnik = {'sf':red[0],'sb':red[1],'dr':red[2],'dp':red[3],'do':red[4],'k':red[5],'t':red[6],'kl':red[7],'tv':red[8],'tr':red[9],'kp':red[10],'c':red[11],'r':red[12],'o':red[13]}
			lista = [recnik]
			broj = broj + int(red[11])
			for i in lista:
				print("{0:2}|{1:2}|{2:4}|{3:4}|{4:4}|{5:4}|{6:4}|{7:2}|{8:2}|{9:2}|{10:2}|{11:3}|{12:3}|{13:1}".format(i['sf'],i['sb'],i['dr'],i['dp'],i['do'],i['k'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c'],i['r'],i['o']))
	print("Ukupna zarada je: ", broj)

def prosecnaOcena():
	otvori = open("rezervacija.txt", "r")
	redovi = otvori.readlines()
	otvori.close()
	recnik = {}
	broj1 = 0
	broj2 = 0
	for red in redovi:
		red = red.split("|")
		if red[13] != 0:
			recnik = {'sf':red[0],'sb':red[1],'dr':red[2],'dp':red[3],'do':red[4],'k':red[5],'t':red[6],'kl':red[7],'tv':red[8],'tr':red[9],'kp':red[10],'c':red[11],'r':red[12],'o':red[13]}
			lista = [recnik]
			broj2 = broj2 + int(red[13])
			broj1 =  broj1 + 1
			prosek = broj2/broj1
			for i in lista:
				print("{0:2}|{1:2}|{2:4}|{3:4}|{4:4}|{5:4}|{6:4}|{7:2}|{8:2}|{9:2}|{10:2}|{11:3}|{12:3}|{13:1}".format(i['sf'],i['sb'],i['dr'],i['dp'],i['do'],i['k'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c'],i['r'],i['o']))
	print("Prosecna ocena: ", prosek)

def odjava():
	print("Ukucaj 'exit' za odjavu: ")
	if input() == 'exit':
		exit()

main()
