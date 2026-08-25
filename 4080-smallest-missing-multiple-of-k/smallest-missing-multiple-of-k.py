class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        i=1
        while k!=0:
            if k*i not in a:
                return k*i
            i+=1
    

        