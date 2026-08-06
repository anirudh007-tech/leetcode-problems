class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        q=0
        for i in range(n,101):
            q=i
            p=1
            while i>0:
                x=i%10
                p=p*x
                i=i//10
            if p%t==0:
                return q
        