def idays(weights,k,days):
    c=1
    s=0
    for i in weights:
        if i+s<=k:
            s+=i
        else:
            c+=1
            s=i
    return c<=days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
       l=max(weights)
       h=sum(weights)
       while l<h:
            m=(l+h)//2
            if idays(weights,m,days):
                h=m
            else:
                l=m+1
       return l

       