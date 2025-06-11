class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        maxf = 0
        hm = {}
        res = 0
        
        while r < n:
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxf = max(maxf, hm[s[r]]) #maintain
            
            if (r - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res
