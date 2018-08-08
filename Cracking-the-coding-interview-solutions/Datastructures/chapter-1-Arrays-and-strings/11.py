"""
Algorithm.

s = ""
enumerate and count occurrence with Counter() from the collections module.
If there is a number greater than 1 in keys, then return false
"""

from collections import Counter
import unittest

def has_unique_1(inputString):

	cnt = Counter(inputString)
	is_unique = True
	lst = []

	for k, v in cnt.items():
		if v > 1:
			lst.append(k)
	if len(lst) == 0:
		is_unique = True
	else:
		is_unique = False
	return is_unique

def has_unique_2(inputString):

	cnt = Counter(inputString)
	is_unique = True
	lst = []

	for v in cnt.values():
		if v > 1:
			lst.append(k)
	if len(lst) == 0:
		is_unique = True
	else:
		is_unique = False
	return is_unique

class UniquesCharacterCase(unittest.TestCase):
	def test_has_unique(self):
		self.assertEqual(has_unique("secret"), False)
		self.assertEqual(has_unique("secret"), True)

def main():
	unittest.main()

if __name__ == "__main__":
	main()