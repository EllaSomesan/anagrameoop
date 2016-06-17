from anagrame import Anagrame
import sys

anagrame = Anagrame(sys.argv[1])

while True:
	cuvant = input("Cuvantul ('exit' pt terminare): ")
	cuvant = cuvant.strip()
	if cuvant == 'exit':
		break
	print('cuvantul ' + cuvant + ' (sau anagramele lui) apare de ' + str( len( anagrame.anagramele_cuvantului_din_lista( cuvant ) ) ) )

