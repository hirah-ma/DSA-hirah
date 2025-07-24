class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        maxfreq = 0

        for right in range(len(nums)):
            total += nums[right]

            while (right - left + 1) * nums[right] > k + total:
                total -= nums[left]
                left += 1

            maxfreq = max(maxfreq, right - left + 1)
        return maxfreq        
                 


        