class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hm ={}
        # for i in range(len(nums)):
        #     if target - nums[i] in hm :
        #         return [hm[target - nums[i]],i ]
        #     hm[nums[i]] = i 

        #Bs greedy 
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()
        left, right = 0, len(nums)-1
        while left < right :
            s = arr[left][0] + arr[right][0]
            if s == target:
                return [arr[left][1] , arr[right][1]]
            elif s < target:
                left +=1
            else:
                right  -= 1        



        