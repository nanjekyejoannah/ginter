import unittest


def reverse_string(inputString):
	string_list = list(inputString)
	final_string = ""
	strLength = len(inputString)

	try:
		while strLength >= 0:
			letter = string_list.pop()
			final_string = final_string + letter
			strLength = strLength - 1
	except:
		pass

	return final_string

class ReverseStringCase(unittest.Testcase):
	def test_reverse_string(self):
		self.assertEqual(reverse_string("see"), "ees")

def main():
	unittest.main()

if __name__ == "__main__":
	main()
