class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        a=[]
        z=[]
        left=0
        q=list(blocks)
        w=len(q)
        for left in range(w-k+1):
            b=[]
            for i in range(left,left+k):
                b.append(q[i])
            a.append(b)
        for i in a:
            c=i.count("B")
            z.append(abs(k-c))
        return min(z)


        