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
	uloga = input("Unesite ulogu(1-korisnik, 2-recepcioner, 3-administrator): ")
	if uloga == '1':
		import korisnik
                        #-Ovde je pozvana funkcija iz fajla "korisnik" i dodeljen joj je parametar za ulogovanog korisnika
		korisnik.ulogovani_korisnik(k_ime)
	elif uloga == '2':
		import recepcioner
	elif uloga == '3':
		import admin
	else:
		print("Uloga nije prepoznata.")

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
	otvori.write(k_ime + "|" + lozinka + "|" + ime + "|" + prezime + "|" + telefon + "|" + email + "|" + uloga + "\n")
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
