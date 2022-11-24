class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        m = int(l + (r - l)/2)
        # m = (l + r)/2    # This may occur overflow
        while l <= r:
            if nums[m-1] > nums[m]:
                return nums[m]
            
            if nums[0] <= nums[m]:
                l = m + 1
            elif nums[0] > nums[m]:
                r = m - 1
            m = int(l + (r - l)/2)
            print("l:%d r:%d m:%d" % (l,r,m))
        return nums[0]

if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3,4,5,1,2]))
    print(s.findMin([4,5,6,7,0,1,2]))

