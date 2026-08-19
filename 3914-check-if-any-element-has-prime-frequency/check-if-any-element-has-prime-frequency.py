class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        a={}
        w=0
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in a.values():
            c=0
            for j in range(1,i+1):
                if i%j==0:
                    c+=1
            if c==2:
                w=1
        if w==1:
            return True
        else:
            return False
        