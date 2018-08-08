"""

"""
import unittest

def replace(inputString, this, withthis):
	newString = inputString.replace(this, withthis)
	return newString

class ReplaceCase(unittest.TestCase):
	def test_replace(self):
		self.assertEqual(replace("sd j", " ", "%20"), "sd" + '%20j')

def main():
	unittest.main()

if __name__ == "__main__":
	main()

