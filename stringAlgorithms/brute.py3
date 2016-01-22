def strstrBruteForce(str, pattern):
	if not pattern:
		return 0
	for i in range(len(str) - len(pattern) + 1):
		stri = i
		patterni = 0
		while stri < len(str) and patterni < len(pattern) and str[stri] == pattern[patterni]:
			stri += 1
			patterni += 1
		if patterni == len(pattern):
			return i
	return -1
	
print(strstrBruteForce('xxxxyzabcdabcdefabc', 'abc'))