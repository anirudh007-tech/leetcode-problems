class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #fixed length sliding window
        maxavg=-1000000000
        left=0
        currsum=0
        for right in range(len(nums)):
            currsum+=nums[right]
            if right>=k-1:
                avg=currsum/k
                maxavg=max(avg,maxavg)
                #subtracting the value on left
                currsum-=nums[left]
                left+=1
        return maxavg
        