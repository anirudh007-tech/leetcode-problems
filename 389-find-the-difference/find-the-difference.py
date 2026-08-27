class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0:
            return t[0]
        a={}
        b={}
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in t:
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        for i in b.keys():
            if i not in a.keys():
                return i
        for i in s:
            if a[i]!=b[i]:
                return i
        