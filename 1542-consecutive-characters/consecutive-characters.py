class Solution:
    def maxPower(self, s: str) -> int:
        c=0
        ma=0
        a=list(s)
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
                ma=max(ma,c)
            else:
                c=0
        return ma+1

        