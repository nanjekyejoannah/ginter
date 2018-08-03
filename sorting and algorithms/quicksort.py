from random import randint

def create_array(size, max):
	from random import randint
	return [randint(0, max) for _ in range(size)]

def quick_sort(a):

	if len(a) <= 1:
		return a

	smaller, equal, larger = [], [], []
	pivot = randint(0, int(len(a)-1))

	for x in a:
		if x < pivot:
			smaller.append(x)
		if x > pivot:
			larger.append(x)
		if x == pivot:
			equal.append(x)
	return quick_sort(smaller) + equal + quick_sort(larger)


# time complexity - nlogn n^2
# space complexity - 0(logn)