class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c=0
        ma=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                c+=1
                ma=max(ma,c)
            else:
                c=0
        return ma+1


        