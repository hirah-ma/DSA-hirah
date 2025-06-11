class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l,r,op=0,0,0
        n= len(nums) #learn
        for i in range(n-2):
            if nums[i]==0:
                op+=1
                for l in range(i,i+3):
                    nums[l]=abs(nums[l]-1)
        if nums[-1 ]==0 or nums[-2]==0 :
            return -1
        return op    


        