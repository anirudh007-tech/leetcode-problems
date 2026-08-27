class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=len(nums)
        q=set(nums)
        if len(q)<s:
            return True
        else:
            return False
        