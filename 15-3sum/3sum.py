class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        w=0
        l=1
        r=len(nums)-1
        q=[]
        z=set()
        while w<len(nums):
            l=w+1
            r=len(nums)-1
            while l<r:
                if nums[w]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[w]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[w]+nums[l]+nums[r]==0:
                    
                    z.add((nums[w],nums[l],nums[r]))
                    r-=1
                    l+=1
            w+=1
        return list(z)


        