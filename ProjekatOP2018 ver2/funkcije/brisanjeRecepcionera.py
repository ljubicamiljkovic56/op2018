def brisanjeRecepcionera():
	print("Brisanje recepcionera")
	otvori  = open("recepcioner.txt", "r")
	for line in otvori:
		print((line.replace("|", " ")).strip())
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
brisanjeRecepcionera()