#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxSumDivThree(vector<int>& nums)
    {
        int k[2][3] = { { 0, 0, 0 }, { 0, 0, 0 } };
        // vector<vector<int>> k = { { 0, 0, 0 }, { 0, 0, 0 } };
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < 3; j++) {
                int temp = k[0][j] + nums[i];
                k[1][temp % 3] = max(k[1][temp % 3], temp);
            }
            for (int j = 0; j < 3; j++) {
                k[0][j] = k[1][j];
            }
        }
        return k[0][0];
    }
};
