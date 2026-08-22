class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a=n
        m=1
        su=0
        while a!=0:
            q=a%10
            su+=q
            m=m*q
            a=a//10
        if n%(su+m)==0:
            return True
        else:
            return False

        
        