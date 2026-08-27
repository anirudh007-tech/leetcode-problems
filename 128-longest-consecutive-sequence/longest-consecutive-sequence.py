class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        l=1
        m=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]-1==nums[i-1]:
                l+=1
            else:
                l=1
            m=max(m,l)
        return m
        