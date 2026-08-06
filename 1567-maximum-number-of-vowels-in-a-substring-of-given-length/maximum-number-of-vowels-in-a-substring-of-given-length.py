class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ma=-111111110
        a=list(s)
        c=0
        left=0
        s=[]
        for right in range(len(a)):
            if a[right] in (["a","e","i","o","u"]):
                c+=1
            if right>=k-1:
                    ma=max(ma,c)
                    if a[left] in (["a","e","i","o","u"]):
                        c-=1
                    left+=1
        return ma



        