class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        h = {}
        for i in range( len(nums)):
            if target - nums[i] in h:
                ans.append(i)
                ans.append(h[target - nums[i]])
            else:
                h[nums[i]] = i
        return ans           
            

        