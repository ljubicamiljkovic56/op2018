import helpf
def main():
	naslov()
	while True:
		admin_meni()
		opcija = input('>>>')
		if opcija == '1':
			formatTabela()
			pregled()
		elif opcija == '2':
			pretragaHotela()
		elif opcija == '3':
			dodajHotel()
		elif opcija == '4':
			dodajRecepcionera()
		elif opcija == '5':
			izmenaHotela()
		elif opcija == '6':
			brisanjeHotela()
		elif opcija == '7':
			brisanjeRecepcionera()
		elif opcija == '8':
			pretragaRecepcionera()
		elif opcija == '9':
			odjava()
		else:
			print("Opcija nije prepoznata")

def naslov():
	print("Hotel Servis")
	print("-------------")

def admin_meni():
	print("1. Pregled svih hotela")
	print("2. Pretraga hotela")
	print("3. Dodavanje hotela")
	print("4. Dodavanje recepcionera")
	print("5. Izmena hotela")
	print("6. Brisanje hotela")
	print("7. Brisanje recepcionera")
	print("8. Pretraga recepcionera")
	print("9. Odjava")

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

def dodajHotel():
	print("Dodavanje novih hotela")
	sifra = input("Unesite sifru(6 cifara): ")
	naziv = input("Unesite naziv hotela: ")
	adresa = input("Unesite adresu hotela: ")
	sobe = input("Unesite broj sobe/soba: ")
	bazen = input("Bazen(da/ne): ")
	rest = input("Restoran(da/ne): ")
	cena = input("Cena: ")
	ocena = input("Procena ocena hotela: ")
	otvori = open("hotel.txt", "a")
	otvori.write(sifra + "|" + naziv + "|" + adresa + "|" + sobe + "|" + bazen + "|" + rest + "|" + cena + "|" + ocena + "|" + "\n")
	otvori.close()
	print("Uspesno dodat novi hotel.")

def dodajRecepcionera():
	print("Dodavanje novih recepcionera")
	k_ime = input("Unesite korisnicko ime recepcionera: ")
	lozinka = input("Unesite lozinku recepcionera:  ")
	ime = input("Unesite ime recepcionera: ")
	prezime = input("Unesite prezime recepcionera: ")
	tel = input("Unesite telefonr recepcionera: ")
	email = input("Unesite email recepcionera: ")
	uloga = '2'
	sifra = input("Unesite sifru hotela u kojem recepcioner radi: ")
	otvori = open("recepcioner.txt", "a")
	otvori.write(k_ime + "|" + lozinka + "|" + ime + "|" + prezime + "|" + tel + "|" + email + "|" + uloga + "|" + sifra + "|" + "\n")
	otvori.close()
	print("Uspesno je dodat novi recepcioner.")

def izmenaHotela():
	print("Izmena hotela")
	print("Prvo se izbrise hotel pa se na njegovom mestu kuca novi.")
	lista = []
	otvori = open("hotel.txt", "r")
	redovi = otvori.readlines()
	recnik = {}
	formatTabela()
	for red in redovi:
		red = red.split("|")
		recnik = {'sf':red[0],'n':red[1],'ad':red[2],'sb':red[3],'b':red[4],'r':red[5],'c':red[6],'o':red[7]}
		lista = [recnik]
		for i in lista:
			print("{0:6}|{1:10}|{2:10}|{3:5}|{4:5}|{5:5}|{6:5}|{7:1}".format(i['sf'],i['n'],i['ad'],i['sb'],i['b'],i['r'],i['c'],i['o']))
	sifra = input("Unesite sifru hotela za brisanje: ")
	lista = []
	broj = 0
	otvori.close()
	otvori = open("hotel.txt", "r")
	for line in otvori:
		if line.split("|")[0] != sifra:
			lista.append(line.strip())
		else:
			broj = 1
	otvori.close()
	if broj == 0:
		print("Sifra hotela nepostojeca.")
	else:
		otvori = open("hotel.txt", "w")
		print(lista[0], file=otvori)
		otvori.close()
		lista.pop(0)
		otvori = open("hotel.txt", "a")
		for i in lista:
			print(i, file=otvori)
		otvori.close()
		print("Brisanje zavrseno.")
		print("Unos novih izmena vezane za hotel.")
		otvori = open("hotel.txt", "a")
		sifra = input("Unesite sifru hotela(6 cifara): ")
		naziv = input("Unesite naziv hotela: ")
		adresa = input("Unesite adresu hotela: ")
		sobe = input("Unesite broj sobe/soba: ")
		bazen = input("Bazen(da/ne): ")
		res = input("Restoran(da/ne): ")
		cena = input("Prosecna cena: ")
		ocena = input("Prosecna ocena: ")
		otvori.write(sifra + "|" + naziv + "|" + adresa + "|" + sobe + "|" + bazen + "|" + res + "|" + cena + "|" + ocena + "|" + "\n")
		otvori.close()
		print("Uspesno izmenjen hotel.")

def brisanjeHotela():
	print("Brisanje hotela")
	lista = []
	otvori = open("hotel.txt", "r")
	redovi = otvori.readlines()
	recnik = {}
	formatTabela()
	for red in redovi:
		red = red.split("|")
		recnik = {'sf':red[0],'n':red[1],'ad':red[2],'sb':red[3],'b':red[4],'r':red[5],'c':red[6],'o':red[7]}
		lista = [recnik]
		for i in lista:
			print("{0:6}|{1:10}|{2:10}|{3:5}|{4:5}|{5:5}|{6:5}|{7:1}".format(i['sf'],i['n'],i['ad'],i['sb'],i['b'],i['r'],i['c'],i['o']))
	sifra = input("Unesite sifru hotela za brisanje: ")
	lista = []
	broj = 0
	otvori.close()
	otvori = open("hotel.txt", "r")
	for line in otvori:
		if line.split("|")[0] != sifra:
			lista.append(line.strip())
		else:
			broj = 1
	otvori.close()
	if broj == 0:
		print("Sifra hotela nepostojeca.")
	else:
		otvori = open("hotel.txt", "w")
		print(lista[0], file=otvori)
		otvori.close()
		lista.pop(0)
		otvori = open("hotel.txt", "a")
		for i in lista:
			print(i, file=otvori)
		otvori.close()
		print("Brisanje zavrseno.")

def formatRecepcioner():
	print("K.ime |Lozinka |Ime     |Prezime |Broj tel.|Email          |Uloga|Sifra hotela")
	print("------+--------+--------+--------+---------+---------------+-----+------------")

def brisanjeRecepcionera():
	print("Brisanje recepcionera")
	lista = []
	otvori  = open("recepcioner.txt", "r")
	redovi = otvori.readlines()
	recnik = {}
	formatRecepcioner()
	for red in redovi:
		red = red.split("|")
		recnik = {'k':red[0],'l':red[1],'i':red[2],'p':red[3],'bt':red[4],'e':red[5],'u':red[6],'sh':red[7]}
		lista = [recnik]
		for i in lista:
			print("{0:10}|{1:10}|{2:10}|{3:8}|{4:9}|{5:10}|{6:5}|{7:6}".format(i['k'],i['l'],i['i'],i['p'],i['bt'],i['e'],i['u'],i['sh']))
	k_ime = input("Unesite korisnicko ime recepcionera za brisanje: ")
	lista = []
	broj = 0
	otvori.close()
	otvori = open("recepcioner.txt", "r")
	for line in otvori:
		if line.split("|")[0] != k_ime:
			lista.append(line.strip())
		else:
			broj = 1
	otvori.close()
	if broj == 0:
		print("Korisnicko ime recepcionera nepostojece.")
	else:
		otvori = open("recepcioner.txt", "w")
		print(lista[0], file=otvori)
		otvori.close()
		lista.pop(0)
		otvori = open("recepcioner.txt", "a")
		for i in lista:
			print(i, file=otvori)
		otvori.close()
		print("Brisanje zavrseno.")

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

def odjava():
	print("Ukucaj 'exit' za odjavu: ")
	if input() == 'exit':
		exit()
main()
