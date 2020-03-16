import helpf
def main():
	naslov()
	while True:
		meni()
		opcija = input('>>>')
		if opcija == '1':
			prijava()
		elif opcija == '2':
			registracija()
		elif opcija == '3':
			formatTabela()
			pregled()
		elif opcija == '4':
			pretragaHotela()
		elif opcija == '5':
			ocenaHotela()
		elif opcija == '6':
			odjava()
		else:
			print('Opcija nije prepoznata')

def naslov():
	print("Hotel Servis")
	print("-------------")

def meni():
	print("1. Prijava na sistem")
	print("2. Registracija")
	print("3. Pregled svih hotela")
	print("4. Pretraga hotela")
	print("5. Pregled najboljih hotela")
	print("6. Odjava")

def prijava():
	k_ime = input("Unesite korisnicko ime: ")
	lozinka = input("Unesite lozinku: ")
	otvori = open("registrovani_k.txt", "r")
	redovi = otvori.readlines()
	uloga = '1'
	for red in redovi:
		red = red.split("|")
		if red[0] == k_ime and red[1] == lozinka:
			otvori.close()
			import korisnik
			return 
	otvori.close()
	otvori = open("recepcioner.txt", "r")
	redovi = otvori.readlines()
	uloga = '2'
	for red in redovi:
		red = red.split("|")
		if red[0] == k_ime and red[1] == lozinka:
			otvori.close()
			import recepcioner
			return 
	otvori.close()
	otvori = open("administrator.txt", "r")
	redovi = otvori.readlines()
	uloga = '3'
	for red in redovi:
		red = red.split("|")
		if red[0] == k_ime and red[1] == lozinka:
			otvori.close()
			import admin
			return
	else:
		print("Uneli ste neispravne podatke.")
	otvori.close()

def registracija():
	print("Registracija")
	k_ime = input("Unesite korisnicko ime: ")
	lozinka = input("Unesite lozinku: ")
	ime = input("Unesite ime: ")
	prezime = input("Unesite prezime: ")
	telefon = input("Unesite broj telefona: ")
	email = input("Unesite email: ")
	uloga = '1'
	otvori = open("registrovani_k.txt", "a")
	otvori.write(k_ime + "|" + lozinka + "|" + ime + "|" + prezime + "|" + telefon + "|" + email + "|" + uloga + "|" + "\n")
	otvori.close()
	print("Uspesno ste se registrovali.")

def formatTabela():
	print("Sifra |Naziv     |Adresa    |Soba |Bazen|Rest.|Cena |Ocena")
	print("------+----------+----------+-----+-----+-----+-----+------")
def pregled():
	lista = []
	fajl = open("hotel.txt","r")
	redovi = fajl.readlines()
	fajl.close()
	recnik = {}
	for red in redovi:
		red = red.split("|")
		recnik = {'sf':red[0],'n':red[1],'ad':red[2],'sb':red[3],'b':red[4],'r':red[5],'c':red[6],'o':red[7]}
		lista = [recnik]
		for i in lista:
			print("{0:6}|{1:10}|{2:10}|{3:5}|{4:5}|{5:5}|{6:5}|{7:1}".format(i['sf'],i['n'],i['ad'],i['sb'],i['b'],i['r'],i['c'],i['o']))

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

def ocenaHotela():
	lista = []
	otvori = open("hotel.txt", "r")
	redovi = otvori.readlines()
	recnik = {}
	formatTabela()
	for red in redovi:
		red = red.split("|")
		recnik = {'sf':red[0],'n':red[1],'ad':red[2],'sb':red[3],'b':red[4],'r':red[5],'c':red[6],'o':red[7]}
		lista = [recnik]
		if int(red[7]) > 4:
			for i in lista:
				print("{0:6}|{1:10}|{2:10}|{3:5}|{4:5}|{5:5}|{6:5}|{7:1}".format(i['sf'],i['n'],i['ad'],i['sb'],i['b'],i['r'],i['c'],i['o']))
	otvori.close()

def odjava():
	print("Ukucaj 'exit' za odjavu: ")
	if input() == 'exit':
		exit()

main()
