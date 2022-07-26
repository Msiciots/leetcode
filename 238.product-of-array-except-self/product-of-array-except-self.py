class Solution:
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)
        l = 1
        r = 1
        n = len(nums)
        for i in range(1, n):
            l *= nums[i - 1]
            r *= nums[n - i]
            ans[i] *= l
            ans[n - 1 - i] *= r

        return ans
            
