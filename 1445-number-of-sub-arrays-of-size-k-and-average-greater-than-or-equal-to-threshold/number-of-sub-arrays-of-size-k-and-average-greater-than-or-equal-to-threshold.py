class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        first_window=arr[:k]
        currentsum=sum(first_window)
        count=0
        if currentsum/k>=threshold:
            count+=1
        for i in range(k,len(arr)):
            currentsum=currentsum+arr[i]-arr[i-k]
            if currentsum/k>=threshold:
                count+=1
        return count
        