#include <vector>
using namespace std;
 
class Fenwick_Tree_Sum
{
    vector<int> tree;
    Fenwick_Tree_Sum(const vector<int>& Arg)
    {
        tree.resize(Arg.size());
 
        for(int i = 0 ; i<tree.size(); i++)
            increase(i, Arg[i]);
 
    }
 
    void increase(int i, int delta)
    {
        for (; i < (int)tree.size(); i |= i + 1)
            tree[i] += delta;
    }
 
    int getsum(int left, int right)
    {
        return sum(right) - sum(left-1); 
    }
 
    int sum(int ind)
    {
        int sum = 0;
        while (ind>=0)
        {
            sum += tree[ind];
            ind &= ind + 1;
            ind--;
        }
        return sum;
    }
};