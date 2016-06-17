import unittest
from tempfile import mkstemp
import os

from anagrame import Anagrame

class TesteazaAnagramele(unittest.TestCase):
	def setUp(self):
		"""pregatim testele deschizand un fisier temporar (care nu are niciun cuvant in el), pentru a putea folosi metodele auxiliare din clasa Anagrame """
		self.fisier, self.nume_fisier = mkstemp()

		#instanta clasei Anagrame careia ii testam din metode
		self.anagrame = Anagrame(self.nume_fisier)

	def tearDown(self):
		"""stergem fisierul temporar deschis in setUp"""
		try:
		    os.remove(self.nume_fisier)
		except OSError as motiv:
		    print(motiv)

	def test_verificarea_1(self):
		t1 = ['aab', 'aba', 'baa', 'AAB', 'AAC']
		agr = self.anagrame.genereaza_anagramele(t1)
		self.assertTrue( len( agr['aab'] ) == 4 )
	
	def test_verificarea_2(self):
		t1 = ['aab', 'aba', 'baa', 'AAB', 'AAC']
		agr = self.anagrame.genereaza_anagramele(t1)
		self.assertNotEqual( len( agr['BAA'] ), 4 )

if __name__ == '__main__':
	unittest.main()
