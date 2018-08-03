def binary_search (arr, val):

	if len(arr) == 0 or (len(arr) == 1 and arr[0] != val):
		return False

	mid = int(len(arr)/2)

	if val == mid:
		return True

	if val < mid:
		return binary_search (arr[:int(len(arr)/2)], val)
	if val > mid:
		return binary_search(arr[(int((len(arr)/2)+1)):], val)

print (binary_search([0,1,2,3,4,5,6,7,8,9], 6))

# complexity logn
# Used to search sorted arrays
# space complexity (o(1))
