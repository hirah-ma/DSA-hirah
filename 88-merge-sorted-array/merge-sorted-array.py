# from typing import List hhhhhard solution gap method

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         l = m + n
#         gap = (l + 1) // 2

#         while gap > 0:
#             left = 0
#             right = gap
#             while right < l:
#                 # left in nums1, right in nums1
#                 if left < m and right < m:
#                     if nums1[left] > nums1[right]:
#                         nums1[left], nums1[right] = nums1[right], nums1[left]

#                 # left in nums1, right in nums2
#                 elif left < m and right >= m:
#                     if nums1[left] > nums2[right - m]:
#                         nums1[left], nums2[right - m] = nums2[right - m], nums1[left]

#                 # left in nums2, right in nums2
#                 else:
#                     if nums2[left - m] > nums2[right - m]:
#                         nums2[left - m], nums2[right - m] = nums2[right - m], nums2[left - m]

#                 left += 1
#                 right += 1

#             if gap == 1:
#                 break
#             gap = (gap + 1) // 2
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = m + n  # total valid elements
        gap = (l + 1) // 2

        def get_val(idx):
            if idx < m:
                return nums1[idx]
            else:
                return nums2[idx - m]

        def set_val(idx, val):
            if idx < m:
                nums1[idx] = val
            else:
                nums2[idx - m] = val

        while gap > 0:
            left = 0
            right = gap
            while right < l:
                if get_val(left) > get_val(right):
                    temp = get_val(left)
                    set_val(left, get_val(right))
                    set_val(right, temp)
                left += 1
                right += 1
            if gap == 1:
                break
            gap = (gap + 1) // 2

        # Copy nums2 into nums1’s tail
        for i in range(n):
            nums1[m + i] = nums2[i]
                   