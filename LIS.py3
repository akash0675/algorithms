N = int(input())
arr = []
lis = []
for i in range(N):
	a = int(input())
	arr.append(a)
	lis.append(1)
for i in range(1, N):
	for j in range(0, i):
		if arr[i] > arr[j] and lis[i] < lis[j] + 1:
			lis[i] = lis[j] + 1
print(max(lis))
