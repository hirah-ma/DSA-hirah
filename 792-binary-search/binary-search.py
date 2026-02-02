class Solution:
    def search(self, a: List[int], target: int) -> int:
        l, r = 0, len(a) - 1
        while(l<=r):
            mid = l + r
            mid = mid//2
            if a[mid] == target:
                return mid
            elif a[mid] > target :
                r = mid - 1
            elif a[mid] < target:
                l =  mid +1

        return -1        
        