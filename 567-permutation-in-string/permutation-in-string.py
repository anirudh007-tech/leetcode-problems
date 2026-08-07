class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c={}
        d={}
        w=len(s1)
        left=0
        for i in s1:
            d[i]=d.get(i,0)+1
        for i in range(len(s2)):
            c[s2[i]]=c.get(s2[i],0)+1
            if i>=w-1:
                if c==d:
                    return True
                if c[s2[left]]==1:
                    c.pop(s2[left])

                else:
                    c[s2[left]]-=1
                left+=1
        return False

        