class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a="".join(map(str,digits))
        a=int(a)
        a=a+1
        a=str(a)
        b=[]
        for i in a:
         b.append(int(i))
        return b

    

        