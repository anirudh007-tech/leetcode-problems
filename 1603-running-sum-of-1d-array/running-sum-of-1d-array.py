class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        ll=[]
        for i in nums:
            sum=sum+i
            ll.append(sum)
        return ll


        