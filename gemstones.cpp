#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	int t;
	cin >> t;
	int N = t;
	int count = 0;
	int arr[26] = {0};
	while(t--){
		string str;
		cin	>> str;
		int length = str.size();
		for(int i = 0; i < length; ++i){
			if(binary_search(str.begin(), str.end(), str[i]))
				arr[str[i] - 97]++;
		}
	}
	for(int j = 0; j < 26; ++j){
		cout<<arr[j] << " ";
		//if(arr[j] == N)
		//	count++;
	}
	cout << count;
	return 0;
}
