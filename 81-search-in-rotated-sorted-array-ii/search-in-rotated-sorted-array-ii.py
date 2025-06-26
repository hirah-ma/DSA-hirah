class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n= len(nums)
        low, high = 0, n-1
        while low<=high :
            mid = low + high
            mid = mid//2

            if nums[mid] == target :
                return True
            if nums[low]== nums[mid] and nums[mid]==nums[high]:
                low = low+1 
                high = high-1
                continue
            elif nums[low]== nums[mid] and nums[mid]!=nums[high]:
                low = low+1 
                
                continue 
            elif nums[low]!= nums[mid] and nums[mid]==nums[high]:
                
                high = high-1
                continue          
            else:
                            
                if nums[low]<= nums[mid]: # this ensures that left is sorted
                    if nums[low]<= target and target <= nums[mid] :
                        high = mid-1
                    else:
                        low=  mid+1    
                else:
                    if nums[mid]<=target and target <= nums[high]:
                        low = mid +1
                    else:
                        high = mid-1
        return False 
        