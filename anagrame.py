from collections import defaultdict
import sys
import os.path
import re

class NumeFisierObligatoriu(Exception):
	def __init__(self, mesaj):
		self._mesaj = mesaj
	def __str__(self):
		return self._mesaj

class Anagrame:

	def __init__(self, nume_fisier=None):
		if nume_fisier is None:
			raise NumeFisierObligatoriu('Numele fisierului din care sa citesc anagramele trebuie dat ca parametru')

		if not os.path.isfile(nume_fisier):
			raise FileNotFoundError

		self._cuvinte = self._citeste_cuvintele(nume_fisier)
		self._anagrame = self.genereaza_anagramele()

	def _citeste_cuvintele(self, fisier):
		cuvinte = []
		with open(fisier) as f:
			#citim fisierul linie cu linie
			for linie_text in f:
				#fiecare linie o impartim in cuvinte
				#un cuvant este orice sir de caractere delimitat de non-word characters ( \W ca regular expression) 
				for cuvant in re.compile("\W").split(linie_text):
					#tinem doar cuvintele care nu sunt sir vid dupa ce le golim de caracterele whitespace
					if cuvant.strip():
						cuvinte.append( cuvant.strip() )
		return cuvinte

	def genereaza_anagramele(self, lista_cuvinte=None):
		"""
		- structura de date in care tinem anagramele e un dictionar unde cheia e valoarea canonica a anagramei, iar valoarea e o lista ce contine toate aparitiile unei anagrame in lista de cuvinte 
		- pentru a afla numarul de aparitii al unei anagrame, e suficient sa ne uitam la lungimea listei de aparitii
		- "valoarea canonica" a anagramei o consideram a fi cuvantul format din sortarea alfabetica a literelor anagramei, dupa ce aceasta a fost convertita la litere mici
		"""

		if lista_cuvinte is None:
			lista_cuvinte = self._cuvinte

		anagrame = defaultdict(list)
		for cuvant in lista_cuvinte:
			cuvant = cuvant.lower()
			anagrama = "".join( sorted( cuvant ) )
			anagrame[ anagrama ].append( cuvant )
		return anagrame

	def anagramele_cuvantului_din_lista(self, cuvant, lista_cuvinte=None):
		cheia = "".join( sorted( cuvant.lower() ) )
		#daca nu e data lista_cuvinte ca parametru, returnam anagramele din fisier
		if lista_cuvinte is None:
			return self._anagrame[cheia]
		anagrame = self.genereaza_anagramele( lista_cuvinte )
		return anagrame[cheia]

	#bonus
	def printeaza_toate_anagramele(self, lista_cuvinte=None):
		anagrame = genereaza_anagramele(lista_cuvinte)
		for cheia, cuvinte in anagrame.items():
			if len(cuvinte) > 1:
				print( cheia, ' apare de ' + str( len(cuvinte) ) + ' ori ca anagrama: ', cuvinte )
	def cuvintele(self):
		return self._cuvinte
