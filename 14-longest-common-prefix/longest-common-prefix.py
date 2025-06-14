class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        if len(strs)==1:
            return strs[0]
        for i in range(len(strs[0])):
            letter = strs[0][i]
            f = 0
            for j in range(1,len(strs)):
                if i<len(strs[j]):
                    if strs[j][i]== letter:
                        f= 1
                    else:
                        f = 0
                        break
                else:
                    f=0
                    break        
            if f==1:
                s = s+ letter
            else:
                break    
        return s                    

        