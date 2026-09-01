class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        a=[]
        b=[]
        for i in range(1,n+1):
            if i in target:
                b.append(i)
                a.append("Push")
            else:
                a.append("Push")
                a.append("Pop")
            if b==target:
                break
        return a
        