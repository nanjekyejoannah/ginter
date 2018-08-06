# Notes 

# Best case = O(1)
# Worst Case and Average Case = n^2
# It is inplace and stable
# space complexity o(n)

def bubble_sort(listt):
	for i, num in enumerate(listt):
		try:
			if listt[i+1] > num:
				listt[i], listt[i+1] = listt[i+1], num
				bubble_sort(listt)
		except IndexError:
			pass
	return listt

