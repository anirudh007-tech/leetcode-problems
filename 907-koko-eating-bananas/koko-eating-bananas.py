def eat(piles,k,h):
    o=0
    for i in piles:
        o+=math.ceil(i/k)
    return o<=h
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       l=1
       hi=max(piles)
       while l<hi:
            m=(l+hi)//2
            if eat(piles,m,h):
                hi=m
            else:
                l=m+1
       return l
    

        