class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        if k==1:
            ma=-1
            for i in a:
                if a[i]==1:
                    ma=max(ma,i)
            return ma
        if k==len(nums):
            ma=max(a.keys())
            return ma
        m=-1
        if a[nums[0]]==1:
            m=max(m,nums[0])
        if a[nums[-1]]==1:
            m=max(m,nums[-1])
        return m




        