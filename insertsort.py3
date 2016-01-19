def insertionSort(alist):
	count = 0
	for index in range(1, len(alist)):

		currentvalue = alist[index]
		position = index
		#print('currentvalue: ',currentvalue)
		#print('position: ',position)

		while position > 0 and alist[position-1] > currentvalue:
			alist[position] = alist[position-1]
			#print(*alist)

			position -= 1
			count += 1

		alist[position] = currentvalue
		#print(*alist)
	print(count)


N = int(input())
alist = [int(i) for i in input().split()]		
insertionSort(alist)
#print(*alist)