class Solution:
    def threeSum(self, nums):
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i-1] and i != 0:
                continue
            l = i + 1
            r = len(nums) - 1
            
            while l < r:

                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1


        return res

if __name__ == "__main__":
    s = Solution()
    s.threeSum([-2, 0, 1, 1, 2])
