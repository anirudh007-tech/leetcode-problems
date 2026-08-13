class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ls=0
        rs=0
        s=0
        a=[]
        for i in nums:
            s+=i
            a.append(s)
        ts=a[-1]
        for i in range(len(nums)):
            if i==0:
                ls=0
            else:
                ls=a[i-1]
            rs=ts-a[i]
            if ls==rs:
                return(i)
        return -1
        
        