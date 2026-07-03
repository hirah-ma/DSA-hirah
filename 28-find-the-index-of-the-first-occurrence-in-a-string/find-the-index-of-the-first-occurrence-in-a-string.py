class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, h = needle, haystack
        m, n = len(haystack),  len(needle)
        if n > m:
            return -1
        f= True
        for i in range(m-n +1):
            f= True            
            for j in range(n):
               if l[j] != h[i+j]:
                f = False
                break
            if f is True:
                return i
        
        if  f is False:
            return -1            
                



        