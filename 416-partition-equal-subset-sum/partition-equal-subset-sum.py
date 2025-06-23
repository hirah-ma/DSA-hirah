class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def f(arr, target):
            n= len(nums)
            dp = [[False for _ in range(target + 1)] for _ in range(n)]
            for i in range(n):
                dp[i][0]= True
            if arr[0]<=target:
                dp[0][arr[0]] = True
            for ind in range(n):
                for j in range(target +1):
                    take = dp[ind-1][j]
                    nottake = False
                    if arr[ind]<=target:
                        nottake = dp[ind-1][j - arr[ind]]
                    dp[ind][j] = take or nottake           
            return dp[n-1][target]
        
        totsum = sum(nums)
        if totsum%2: return False
        s= totsum//2
        return f(nums, s)

        