#KMP

def prefixtable(pattern):
	m = len(pattern)
	F = [0]*m
	k = 0
	for q in range(m):
		while k > 0 and pattern[k] != pattern[q]:
			k = F[k-1]
		if pattern[k] == pattern[q]:
			k += 1 
		F[q] = k
	return F

def KMP(text, pattern):
	n = len(text)
	m = len(pattern)
	F = prefixtable(pattern)
	q = 0
	for i in range(n):
		while q > 0 and pattern[q] != text[i]:
			q = F[q-1]
		if pattern[q] == text[i]:
			q += 1
		if q == m:
			return i - m + 1
	return -1			