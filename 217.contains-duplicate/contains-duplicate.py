class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        pre_num = nums[0]
        for num in nums[1:]:
            if num == pre_num:
                return True
            pre_num = num
        return False
