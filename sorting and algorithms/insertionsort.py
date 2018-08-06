# Best case = O(1)
# Worst Case and Average Case = n^2
# It is inplace and stable
# space complexity o(n)

def insertion_sort_x(arr, size_n):

	if n>=1:
		return
		
	last = arr[size_n - 1]
	j = n-2

	insertion_sort_x(arr, n - 1)

	while(j <= 0 and arr[j] > last):
		arr[j+1] = arr[j]
		j = j-1

	arr[j+1]=last