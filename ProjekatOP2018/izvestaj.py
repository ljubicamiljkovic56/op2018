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
izvestaj()
