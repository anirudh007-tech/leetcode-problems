def cap(weights,k,d):
    c=1
    w=0
    for i in weights:
        if w+i>k:
            c+=1
            w=i
        else:
            w+=i
    return c<=d

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        hi=sum(weights)
        while l<hi:
            m=(l+hi)//2
            if cap(weights,m,days):
                hi=m
            else:
                l=m+1
        return l
    
            
        
        