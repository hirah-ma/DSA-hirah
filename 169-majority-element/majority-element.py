class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el = nums[0]
        c = 0 
        for i in range(len(nums)):
            if c == 0:
                el = nums[i]
                c = 1
            elif nums[i] == el :
                c+=1
            else:
                c -= 1  
        c = 0        
        for i in range(len(nums)):
            if nums[i] == el :
                c += 1
        if c > len(nums)//2:
            return el        


        