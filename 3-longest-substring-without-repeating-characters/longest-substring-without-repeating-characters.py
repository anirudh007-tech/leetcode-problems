class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[]
        left=0
        c=0
        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[left])
                left+=1
            a.append(s[right])
            c=max(c,right-left+1)
        return c
        