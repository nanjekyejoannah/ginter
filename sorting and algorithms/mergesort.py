
def create_array(size, max):
	from random import randint
	return [randint(0, max) for _ in range(size)]

def merge(arr1, arr2):
	c = []
	a_idx, b_idx = 0, 0

	while a_idx < len(arr1) and b_idx < len(arr2):
		if arr1[a_idx] < arr2[b_idx]:
			c.append(arr1[a_idx])
			a_idx += 1
		else:
			c.append(arr2[b_idx])
			b_idx += 1

		if a_idx == len(arr1):
			c.append(arr2[b_idx])
		else:
			c.append(arr1[a_idx])

	return c

def merge_sort(arr):

	if len(arr) <= 1:
		return arr

	left, right = merge_sort (arr[:int(len(arr)/2)]), merge_sort (arr[int(len(arr)/2):])

	return merge(left, right)


b = create_array(10, 50)

print (merge_sort(b))

# time complexity - nlogn
# space complexity - 0(n)




