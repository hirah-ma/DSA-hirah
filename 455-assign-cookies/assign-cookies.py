class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l=0
        r=0
        g.sort()
        s.sort()
        
        while l<len(g) and r<len(s): #easy greedy
            if s[r] >= g[l]:
                l+=1
                
            r+=1 
        return l          