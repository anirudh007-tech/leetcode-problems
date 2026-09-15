class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        r=len(nums)-1
        p=0
        while p<=r:
            if nums[p]==0:
                temp=nums[p]
                nums[p]=nums[l]
                nums[l]=temp
                p+=1
                l+=1
            elif nums[p]==2:
                temp=nums[p]
                nums[p]=nums[r]
                nums[r]=temp
                r-=1
            else:
                p+=1

        