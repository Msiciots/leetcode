class Solution:
    def canJumpFromPosition(self,pos: int,nums: List[int],memo):
        if memo[pos]!='u':
            return True if memo[pos]=='g' else False
        furthestJump = min(pos+nums[pos],len(nums)-1)
        for i in range (pos+1,furthestJump+1):
            if self.canJumpFromPosition(i,nums,memo):
                memo[pos]='g'
                return True
        memo[pos] = 'b'
        return False
    def canJump(self, nums: List[int]) -> bool:
        memo = ['u']*len(nums)
        memo[len(nums)-1] = 'g'
        return self.canJumpFromPosition(0,nums,memo)

