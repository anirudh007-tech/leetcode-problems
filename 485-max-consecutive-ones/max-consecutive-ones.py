class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ma=0
        a=0
        for i in nums:
            if i==1:
                a+=1
                ma=max(ma,a)
            else:
                a=0
        return ma

        