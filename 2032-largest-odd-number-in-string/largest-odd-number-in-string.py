class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        # for i in range(n-1):
        #     return int(num)
        for i in range(len(num)-1,-1, -1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""        

        