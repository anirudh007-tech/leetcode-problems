class Solution:
    def reverse(self, x: int) -> int:
        s=x
        rev=0
        x=abs(x)
        while x:
            i=x%10
            rev=rev*10+i
            x=x//10
        if s<0:
            rev=-1*rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
        

        