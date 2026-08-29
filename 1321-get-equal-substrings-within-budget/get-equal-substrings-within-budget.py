class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=0
        le=0
        m=0
        ts=0
        for i in range(len(s)):
            ts+=abs(ord(s[i])-ord(t[i]))
            while ts>maxCost:
                ts-=abs(ord(s[l])-ord(t[l]))
                l+=1
            m=max(m,i-l+1)
        return m
            