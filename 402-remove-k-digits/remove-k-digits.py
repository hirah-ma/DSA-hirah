class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        n= len(num)
        for i in range(n):
            while st and k>0 and int(st[-1])>int(num[i]):
                st.pop()
                k-=1
            st.append(num[i]) #hg

        if k!=0:
            while k>0:
                st.pop()
                k-=1
        s = ''.join(st)
        if s!='':  
            numb = s.lstrip("0")
            if numb=='': numb='0'
        else :
            numb='0'    
        return numb        
        