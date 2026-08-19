class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w=0
        w2=0
        ww=list(word1)
        we=list(word2)
        a=[]
        while w<len(word1) and w2<len(word2):
            a.append(word1[w])
            a.append(word2[w2])
            w+=1
            w2+=1
        a.append(word1[w:])
        a.append(word2[w2:])
        return "".join(a)
        