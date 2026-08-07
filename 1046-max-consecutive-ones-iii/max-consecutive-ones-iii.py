class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zc=0
        ma=0
        left=0
        for  right in range(len(nums)):
            if nums[right]==0:
                zc+=1
            while zc>k:
                if nums[left]==0:
                    zc-=1
                left+=1
            ma=max(ma,right-left+1)
        return ma
