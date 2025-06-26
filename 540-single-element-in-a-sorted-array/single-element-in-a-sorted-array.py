class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # [1,1,2,2,3,4,4,5,5]
        n = len(nums)
        if n==1:
            return nums[0]
        low = 0 
        high = n-1
        while(low<=high):
            mid = (low+ high)//2
            if (mid == n-1 and nums[mid]!= nums[mid-1]) or (mid == 0 and  nums[mid]!= nums[mid+1]):
                return nums[mid]
            if mid +1 < n and mid-1 >=0:
                if nums[mid]!= nums[mid-1] and nums[mid]!= nums[mid+1]:
                    return nums[mid]
                elif mid%2==1 and nums[mid+1] == nums[mid]:
                    high= mid-1
                elif mid%2==0 and nums[mid-1] == nums[mid]:
                    high= mid-2
                elif  mid%2==1 and nums[mid]==nums[mid-1] :
                    low = mid+1
                elif mid%2==0 and nums[mid]== nums[mid+1]:
                    low = mid+2

        return -1            