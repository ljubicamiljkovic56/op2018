import helpf
def main():
	formatTabela()
	proba()
def formatTabela():
	print("Sifra |Naziv     |Adresa    |Soba |Bazen|Rest.|Cena |Ocena")
	print("------+----------+----------+-----+-----+-----+-----+------")
def proba():
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
main()
