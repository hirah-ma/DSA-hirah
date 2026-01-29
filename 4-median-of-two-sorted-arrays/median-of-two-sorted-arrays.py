class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        a  = []
        while i< len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                a.append(nums1[i])
                i = i+1
            else:
                a.append(nums2[j])
                j = j+1
        if i<= len(nums1)-1:
            for idx in range(i,len(nums1)):
                a.append(nums1[idx])  
        if j<= len(nums2)-1:
            for idx in range(j,len(nums2)):
                a.append(nums2[idx]) 

        if len(a)%2 == 0:
            return (a[(len(a))//2 - 1]+a[(len(a))//2 ] )/ 2
        else:
            return  a[(len(a))//2]                        

        