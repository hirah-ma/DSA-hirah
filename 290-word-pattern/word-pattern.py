class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()
        h= {}
        v= set()
        p = True
        if  len(pattern) != len(l):
            return False
        for i in range(len(l)):
            
            if l[i] not in h and pattern[i] not in v:
                h[l[i]] = pattern[i]
                v.add(pattern[i])
            elif l[i] not in h and pattern[i] in v:
                p = False
                break    
            elif l[i] in h:
                if  pattern[i] != h[l[i]]:
                    p = False 
                    break    
        return p      