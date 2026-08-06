class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        maxavg=-100000000
        su=0
        left=0
        c=0
        for right in range(len(arr)):
            su=su+arr[right]
            if right>=k-1:
                avg=su/k
                su-=arr[left]
                left+=1
                if avg>=threshold:
                    c+=1
        return c

        