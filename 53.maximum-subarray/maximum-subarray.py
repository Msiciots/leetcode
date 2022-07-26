class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            max_sum[i] = max([max_sum[i - 1] + nums[i], nums[i]])

        a = max([10, 2])
        print(a)
        return max(max_sum)

    


if __name__ == "__main__":
    s = Solution()

    print(s.maxSubArray([1, -5, 3]))
