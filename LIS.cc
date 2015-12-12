#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> arr;
    vector<int> lis;
    int a;
    for(int i = 0; i < n; ++i){
        cin >> a;
        arr.push_back(a);
        lis.push_back(1);
    }
    for(int i = 1; i < n; ++i){
        for(int j = 0; j < i; ++j){
            if(arr[i] > arr[j] and lis[i] < lis[j] + 1)
                lis[i] = lis[j] + 1;
        }
    }
    cout << *max_element(lis.begin(), lis.end());
}
