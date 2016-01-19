#gemstones
def inter(a, b):
	return list(set(a) & set(b))

N = int(input())
a = list(input())
for i in range(N-1):
	b = list(input())
	a = inter(a, b)
print(len(a))