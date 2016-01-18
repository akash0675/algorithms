N = int(input())
lis = []
lis1 = []

for i in range(N):
	a = int(input())
	lis.append(a)
	lis1.append(1)

for i in range(N):
	if i-1 > 0:
		if lis[i-1] < lis[i]:
			lis1[i] = lis1[i-1] + 1
		else:
			j = i
			while j > 0 and lis[j-1] > lis[j]:
				lis1[j-1] = max(lis1[j-1], lis1[j]+1)
				j-=1

total = sum(lis1)
print(total)