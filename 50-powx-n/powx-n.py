class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if n<0:
            x=1/x
            n=-n
        res=1.0
        cp=x
        while n>0:
            if n%2==1:
                res*=cp
            cp*=cp
            n//=2
        return res
        