

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0  # Minimum jumps to reach index 0 is 0

        for i in range(n):
            max_jump = nums[i]
            for j in range(1, max_jump + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[n - 1]

        
