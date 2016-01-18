# quick sort
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    print("Here's the pivot: ",pivot)# Start outside the area to be partitioned
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    print(*myList[left:right])
    return right

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList

myList = [5, 8, 1, 3, 7, 9, 2]
sortedList = quicksort(myList,0,len(myList)-1)
print(*sortedList)