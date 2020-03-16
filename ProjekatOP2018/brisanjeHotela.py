def brisanjeHotela():
	print("Brisanje hotela")
	otvori  = open("hotel.txt", "r")
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
brisanjeHotela()