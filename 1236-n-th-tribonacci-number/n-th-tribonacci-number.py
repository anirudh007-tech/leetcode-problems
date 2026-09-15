class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        d=[0]*(n+1)
        d[1]=1
        d[2]=1
        for i in range(3,n+1):
         d[i]=d[i-1]+d[i-2]+d[i-3]
        return d[n]
    
        