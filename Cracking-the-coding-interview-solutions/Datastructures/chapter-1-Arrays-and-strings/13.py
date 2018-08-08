from collections import Counter
import unittest

def remove_duplicates(inputString):
	return ''.join(set(list(inputString)))


class RemoveDuplicateCase(unittest.TestCase):
	def test_remove_duplicates(self):
		self.assertEqual(remove_duplicates("seee"), "se")

def main():
	unittest.main()

if __name__ = "__main__":
	main()

