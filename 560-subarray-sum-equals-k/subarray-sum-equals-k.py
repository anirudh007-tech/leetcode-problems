class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={0:1}
        b=[]
        s=0
        ls=0
        c=0
        for i in range(len(nums)):
            s+=nums[i]
            ls=s-k
            if ls in a.keys():
                c+=a[ls]
            if s in a.keys():
                a[s]+=1
            else:
                a[s]=1
        return c
