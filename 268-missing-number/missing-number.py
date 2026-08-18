class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=len(nums)
        s=0
        s1=0
        for i in range(0,a +1):
            s+=i
        s1=sum(nums)
        return s-s1
        