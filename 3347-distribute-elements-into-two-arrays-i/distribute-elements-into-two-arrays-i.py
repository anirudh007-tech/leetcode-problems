class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1=[]
        a2=[]
        a1.append(nums[0])
        a2.append(nums[1])
        for i in range(2,len(nums)):
            if a1[-1]>a2[-1]:
                a1.append(nums[i])
            else:
                a2.append(nums[i])
        for i in a2:
            a1.append(i)
        return a1

        