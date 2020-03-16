def provera():
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
provera()