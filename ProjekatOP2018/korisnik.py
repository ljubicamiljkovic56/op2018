import helpf
#def main():
        #- U sustini funkcija main(koju sam zakomentarisao) je zamenjena sa funkcijom "ulogovani_korisnik()"
        #- Iste su samo moja ima parametar "Korisnicko_ime" koji je prosledjen u glavnom meniju
def ulogovani_korisnik(Korisnicko_ime):
	naslov()
	while True:
		korisnik_meni()
		opcija = input('>>>')
		if opcija == '1':
			formatTabela()
			pregled()
		elif opcija == '2':
			pretragaHotela()
		elif opcija == '3':
			ocenaHotela()
		elif opcija == '4':
				#- rezervacija() i pregledRezervacija() koriste Korisnicko ime tako da sam im dodelio parametar
			rezervacija(Korisnicko_ime)
		elif opcija == '5':
			pregledRezervacija(Korisnicko_ime)
		elif opcija == '6':
			odjava()
		else:
			print("Opcija nije prepoznata.")
                #- Funkcija je rekurzivna (poziva samu sebe), a na dnu ovog fajla sam zakomentarisao stari poziv "main()"
	ulogovani_korisnik(Korisnicko_ime)

def naslov():
	print("Hotel Servis")
	print("-------------")

def korisnik_meni():
	print("1. Pregled svih hotela")
	print("2. Pretraga hotela")
	print("3. Pregled najboljih hotela")
	print("4. Rezervacija")
	print("5. Pregled rezervacija")
	print("6. Odjava")

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

def rezervacija(Korisnicko_ime):
	print("Rezervacija")
	otvori = open("rezervacija.txt", "a")
	sifra = input("Unesite sifru hotela(6 cifara):  ")
	soba = input("Unesite broj sobe/soba: ")
	dat1 = input("Datum i vreme rezervacije(yyyy-mm-dd hh:mm): ")
	dat2 = input("Datum prijave(yyyy-mm-dd hh:mm): ")
	dat3 = input("Datum odjave(yyyy-mm-dd hh:mm): ")
		#- Ovde je za kreiranje rezervacije automatski izgenerisan korisnik
	korisnik = Korisnicko_ime
	tip = input("Unesite tip sobe(apartman/soba): ")
	klima = input("Klima(da/ne): ")
	tv = input("TV(da/ne): ")
	terasa = input("Terasa(da/ne): ")
	kupatilo = input("Kupatilo, deljeno ili ne(da/ne): ")
	cena = input("Cena po nocenju: ")
	rez = input("Rezervacija (nije zapoceta, u toku, zavrsena): ")
	ocena = input("Ocenjivanje hotela (1-5): ")
	otvori = open("rezervacija.txt", "a")
	otvori.write(sifra + "|" + soba + "|" + dat1 + "|" + dat2 + "|" + dat3 + "|" + korisnik + "|" + tip + "|" + klima + "|" + tv + "|" + terasa + "|" + kupatilo + "|" + cena + "|" + rez + "|" + ocena + "\n")
	otvori.close()
	print("Uspesna rezervacija") 

def pregledRezervacija(Korisnicko_ime):
	formatRez()
		#- Posto ne postoji lokalna promenjiva za korisnico ime morao sam je lancano proslediti preko parametra "Korisnicko_ime" 
	rez(Korisnicko_ime)
def formatRez():
	print("Sifra |Sb|Datum rezervac. |Datum prijave   |Datum odjave    |K.ime |Tip sobe|Kl|Tv|Kp|Tr|Cena|Rezerv.|O")
	print("------+--+----------------+----------------+----------------+------+--------+--+--+--+--+----+-------+-")
	#- Posto ne postoji lokalna promenjiva za korisnico ime morao sam je lancano proslediti preko parametra "Korisnicko_ime"
def rez(Korisnicko_ime):
	lista = []
	fajl = open("rezervacija.txt","r")
	redovi = fajl.readlines()
	fajl.close()
	recnik = {}
	for red in redovi:
		red = red.split("|")
			#-Ovde sam ispitao da li rezervacija pripada registrovanom korisniku  
		if red[5] == Korisnicko_ime :
			recnik = {'sf':red[0],'sb':red[1],'dr':red[2],'dp':red[3],'do':red[4],'k':red[5],'t':red[6],'kl':red[7],'tv':red[8],'tr':red[9],'kp':red[10],'c':red[11],'r':red[12],'o':red[13]}
			lista = [recnik]
		for i in lista:
			print("{0:2}|{1:2}|{2:4}|{3:4}|{4:4}|{5:4}|{6:4}|{7:2}|{8:2}|{9:2}|{10:2}|{11:3}|{12:3}|{13:1}".format(i['sf'],i['sb'],i['dr'],i['dp'],i['do'],i['k'],i['t'],i['kl'],i['tv'],i['tr'],i['kp'],i['c'],i['r'],i['o']))

def odjava():
	print("Ukucaj 'exit' za odjavu: ")
	if input() == 'exit':
		exit()
#main()

