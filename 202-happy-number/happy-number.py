def s(n):
    su=0
    while n>0:
        r=n%10
        su+=r*r
        n=n//10
    return su
class Solution:
    def isHappy(self, n: int) -> bool:
       while True:
          if n<10:
            break
          n=s(n)
       if n==1 or n==7:
            return True
       else:
            return False
        

    


        