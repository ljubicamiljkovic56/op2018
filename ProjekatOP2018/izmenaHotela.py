def izmenaHotela():
	print("Izmena hotela")
	print("Prvo se izbrise hotel pa se na njegovom mestu kuca novi.")
	otvori = open("hotel.txt", "r")
	for line in otvori:
		print((line.replace("|", " ")).strip())
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
		otvori.write(sifra + "|" + naziv + "|" + adresa + "|" + sobe + "|" + bazen + "|" + res + "|" + cena + "|" + ocena + "\n")
		otvori.close()
		print("Uspesno izmenjen hotel.")
izmenaHotela()