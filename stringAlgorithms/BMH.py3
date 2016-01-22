#Boyer-Moore-Horspool
def lookUpTable(pattern):
	pattern = list(pattern)
	arr = {}
	for i in pattern:
		arr[pattern[i]] = len(pattern) - i - 1

	return arr
			
pattern = input()
arr = []
arr = lookUpTable(pattern)
print(*arr)