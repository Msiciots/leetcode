#include <iostream>
#include <vector>
using namespace std;
#include "greatest-sum-divisible-by-three.cpp"
int main()
{
    
    // vector<int> input = {3,6,5,1,8};
    // vector<int> input = {1,2,3,4,4};
    vector<int> input = {3,6,5,1,8};
    Solution s;
    int r = s.maxSumDivThree(input);
    cout<<"\nResult: "<<r<<endl;
}