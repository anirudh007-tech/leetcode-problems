class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        left=0
        q=list(s)
        c=0
        for right in range(len(q)):
            while q[right] in a:
                a.remove(q[left])
                left+=1
            a.add(q[right])
            c=max(c,right-left+1)
    
        return c
        