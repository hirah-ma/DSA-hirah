class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #hypothetically
        n= len(nums)
        ans =[-1]*n
        st=[]
        for i in range(2*len(nums)-1,-1,-1):
            while st and st[-1]<=nums[i%n]:
                st.pop()
            if i<n and st:
                ans[i]=st[-1]
            st.append(nums[i%n]) #learn
        return ans            

        