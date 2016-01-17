#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int>& vec, int start, int end){
	int pivot = vec[end];
	int left = start;
	int right = end - 1;
	int flag = 0;
	while(!flag){
		while(left <= right && vec[left] <= pivot)
			left++;
		while(vec[right] >= pivot && right >= left)
			right++;
		if(right < left)
			flag = 1;
		else{
			int temp = vec[left];
			vec[left] = vec[right];
			vec[right] = temp;
		}
	}
	int temp = vec[end];
	vec[end] = vec[left];
	vec[left] = temp;

	return left;
}

vector<int> quickSort(vector<int>& vec, int start, int end){
	if(start < end){
		int split = partition(vec, start, end);
		quickSort(vec, start, split - 1);
		quickSort(vec, split + 1, end);
	}
	return vec;
}

int main(){
	int n;
	cin >> n;
	vector<int> vec;
	for(int i = 0; i < n; i++){
		cin >> vec[i];
	}
	vector<int> sortedList = quickSort(vec, 0, n-1);
	return 0;
}