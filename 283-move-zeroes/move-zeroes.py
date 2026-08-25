class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        r=len(nums)-1
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
            
                

        