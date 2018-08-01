def bubblesort(arr):
	n = len(arr)

	for i in range (0, n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


def bubblesortown(arr):
	length = len(arr)

	for i in range (0,n):
		if arr[i] > arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]


# Notes 

# Best case = O(1)
# Worst Case and Average Case = n^2
# It is inplace and stable

def bubble_sort(listt):
	for i, num in enumerate(listt):
		try:
			if listt[i+1] > num:
				listt[i], listt[i+1] = listt[i+1], num
				bubble_sort(listt)
		except IndexError:
			pass
	return listt

