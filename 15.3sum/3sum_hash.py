class Solution:
    def threeSum(self, nums):
        res = []
        ht = {}
        nums = sorted(nums)
        for i in range(len(nums)):
            ht[nums[i]] = i
        
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                target = 0 - nums[i] - nums[j]
                if (target in ht) and (ht[target] > j):
                    res.append([nums[i], nums[j], target])
                    j = ht[nums[j]]
                j += 1    
                i = ht[nums[i]]
            i += 1 
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-2, 0, 1, 1, 2]))
