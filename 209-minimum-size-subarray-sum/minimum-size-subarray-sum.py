class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        l=0
        s=0
        le=0
        m=100000000
        for i in range(len(nums)):
            s=s+nums[i]
            while s>=target:
                m=min(m,i-l+1)
                s-=nums[l]
                l+=1
        return m

        