class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=0
        a=[]
        for i in nums:
            s=s+i
            a.append(s)
        ls=0
        rs=0
        ts=a[-1]
        for i in range(len(nums)):
            if i==0:
                ls=0
            else:
                ls=a[i-1]
            rs=ts-a[i]
            if ls==rs:
                return i
        return -1
        
        



        