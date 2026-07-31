class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        s=image
        q=[]
        for i in s:
            i.reverse()
            for e in range(len(i)):
                i[e]^=1
        return s

