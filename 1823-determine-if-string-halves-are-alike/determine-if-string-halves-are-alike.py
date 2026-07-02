class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        st = {'a', 'e', 'i', 'o', 'u'}
        cl, cr = 0,0
        for i in s[:len(s)//2]:
            if i.lower() in st:
                cl+=1 
        for i in  s[len(s)//2:]:
            if i.lower() in st:
                cr += 1
        return cl == cr    
        