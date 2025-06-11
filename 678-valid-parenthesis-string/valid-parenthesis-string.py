class Solution:
    def checkValidString(self, s: str) -> bool:
        mini = 0
        maxi =0
        for i in range(len(s)):
            if s[i]=='(':
                mini+=1
                maxi+=1
            elif s[i]==')':
                mini-=1
                maxi-=1 #its not being solved by stacks rather greedy r
            else:
                mini -= 1 #
                maxi += 1
                
            if mini - 1<0:
                mini =0
            if maxi< 0:
                return False     
        if mini ==0 :
            return True
        
        else:
            return False        



        