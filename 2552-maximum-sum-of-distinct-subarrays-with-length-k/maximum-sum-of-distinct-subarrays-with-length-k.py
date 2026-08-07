class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d={}
        c=0
        s=0
        ma=0
        left=0
        for i in range(len(nums)):
            s=s+nums[i]
            d[nums[i]]=d.get(nums[i],0)+1
            if i>=k-1:
                if len(d)==k:
                   ma=max(ma,s)
                s=s-nums[left]
                if d[nums[left]]==1:
                    d.pop(nums[left])
                else:
                    d[nums[left]]-=1
                left+=1
        return ma

        