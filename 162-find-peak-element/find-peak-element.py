class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a= max(nums)
        for i in range(len(nums)):
            if nums[i]==a:
                return i
        