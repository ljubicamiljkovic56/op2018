import helpf
def pretragaRezervacija():
	print("Pretraga rezervacija")
	print("1 - Pretraga po korisniku")
	print("2 - Pretraga po bilo kom kriterijumu")
	unos = input(">>>")
	print("--------------------")
	if unos == '1':
		korisnik = input("Unesite tacno korisnicko ime korisnika: ")
		otvori = open("rezervacija.txt", "r")
		for line in otvori:
			line = line.split("|")
			if line[5] == korisnik:
				print(line)
		print("--------------------")
		otvori.close()
	elif unos == '2':
		inf = input("Unesite informaciju: ")
		otvori = open("rezervacija.txt", "r")
		for line in otvori:
			line = line.split("|")
			for i in line:
				if i == inf:
					print(helpf.listtostring(line))
		print("-----------------------")
		otvori.close()
	else:
		print("Uneli ste nepostojecu opciju.")


pretragaRezervacija()
