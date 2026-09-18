class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=[]
        for i in s:
            if not a:
                a.append(i)
            else:
                if a[-1]==i:
                    a.pop(-1)
                else:
                    a.append(i)
        return "".join(a)


        