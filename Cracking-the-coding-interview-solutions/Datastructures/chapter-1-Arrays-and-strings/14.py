"""
give [s1 and s2] , find if they are anagrams

list s1
list s2

The first is the length is the same
compare characters each character

"""
import unittest

def are_anagrams(s1, s2):
	anagram = True

	if len(s2) != len(s1):
		anagram = False

	s11 = list(s1)
	s22 = list(s2)
	for i in (s11):
		if i not in s22:
			anagram = False
	return anagram

class AnagramCase(unittest.TestCase):
	def test_are_anagrams(self):
		self.assertTrue(are_anagrams("see", "ees"))
		self.assertFalse(are_anagrams("see", "ef"))

def main():
	unittest.main()

if __name__ == "__main__":
	main()