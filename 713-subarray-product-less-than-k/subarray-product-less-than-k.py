class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        c=0
        l=0
        p=1
        for i in range(len(nums)):
            p=p*nums[i]
            while p>=k and l<=i:
                p=p//nums[l]
                l+=1
            c+=(i-l+1)
        return c


        