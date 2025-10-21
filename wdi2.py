#!/usr/bin/env python3
#f = open('protein-matching-IPR002338.fasta') #otwieram plik do czytania
#f = open('krotki.fasta')
import sys

def main():
	# wybierz plik z argv lub domyślnie 'fastalab2.fasta'
	filename = sys.argv[1] if len(sys.argv) > 1 else 'fastalab2.fasta'

	# czytam caly plik na zmienna s
	with open(filename, 'r') as f:
		s = f.read()

	# print(s) wypisuje s (czyli to co w pliku)
	zesplitowane = s.split('>') # splituje informacje o kazdym bialku z osobna
	# jezeli pierwszy element jest pusty (plik zaczyna sie od '>'), usun go
	if len(zesplitowane) > 0 and zesplitowane[0].strip() == '':
		zesplitowane.pop(0)

	sumadlugosci = 0
	sumaleucyny = 0
	licznik = {}
	## print(zesplitowane)
	## print(len(zesplitowane)) debug

	# prepare list of sequence lengths for plotting
	lengths = []

	for i, element in enumerate(zesplitowane, start=1): # przechodzi przez kazdy element listy zesplitowane
		index = element.find("\n") # index przechowuje numer znaku gdzie konczy sie naglowek (gdzie jest pierwsze\n)
		if index == -1:
			sekwencja = ''
		else:
			# element[index+1:] bierze wszystko od pierwszego znaku po naglowku do konca elementu
			# usun nowe linie i spacje, aby uzyskac ciagla sekwencje
			sekwencja = element[index+1:].replace('\n', '').replace(' ', '')

		print("sekwencja:", i)
		print(sekwencja)
		dlugosc = len(sekwencja)
		lengths.append(dlugosc)
		print(dlugosc)
		sumadlugosci += dlugosc
		ileleucyna = sekwencja.count("L") # szukamy ile w sekwencji jest liter L
		sumaleucyny += ileleucyna # sumujemy leucyny po kazdej sekwencji

		for l in sekwencja:
			if l in licznik:
				licznik[l] += 1
			else:
				licznik[l] = 1

	print(licznik)
	liczbasekwencji = i if 'i' in locals() else 0
	print("suma dlugosci:", sumadlugosci)
	print("liczba sekwencji:", liczbasekwencji)
	sredniadlugosc = (sumadlugosci/liczbasekwencji) if liczbasekwencji else 0
	print("srednia dlugosc:", sredniadlugosc)
	print("tyle razy wystepuje leucyna:", sumaleucyny)

    seqs = {}
    aa_counts = {}
    for v in seqs.values ():
        for x in v:
            if x in aa_counts:
                aa_counts[x] += 1
            else:
                aa_counts[x] = 1
    print(len(aa_counts))
    aa_count = {}
    for k, v in seqs.items():
        if k not in aa_count:
            aa_count[k] = {}
        for x in v:
            if x in aa_count[k]:
                aa_count[k][x] += 1
            else:
                aa_count[k][x] = 1
    

seqs_len = {}
for k, v in seqs.items():
    l =  len(v)
    if l in seqs_len:
        seqs_len[l].append(k)
    else:
        seqs_len[l] = [k]

print(len(seqs_len))

n1 = 'aaaa'
n2 = 'aaab'

for i in range(len(n1)):
    if n1[i] != n2[i]:
        h +=1
print(h)

for l in seqs





        

if __name__ == '__main__':
	main()

