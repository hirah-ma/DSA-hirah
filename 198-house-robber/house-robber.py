class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        sprev = 0
        prev = nums[0]
        if n ==1:
            return nums[0]
        for i in range(1,n):
            take = nums[i]
            if i > 1:
                take+=sprev
            ntake = prev
            curri = max(take, ntake)
            sprev = prev
            prev= curri
        return prev         
#
        