class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=[]
        c={}
        d={}
        q=[]
        left=0
        plen=len(p)
        if len(p)>len(s):
            return []
        for i in p:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            if right>=plen-1:
                if d==c:
                    q.append(left)
                r=s[left]
                if d[r]==1:
                    d.pop(r)
                else:
                    d[r]-=1
                left+=1
        return q


        
       