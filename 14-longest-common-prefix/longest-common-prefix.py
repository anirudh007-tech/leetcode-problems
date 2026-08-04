class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        strs.sort()
        f=strs[0]
        l=strs[-1]
        for i in range(min(len(f),len(l))):
            if f[i]!=l[i]:
                return s
            else:
                s=s+f[i]
        return s

                