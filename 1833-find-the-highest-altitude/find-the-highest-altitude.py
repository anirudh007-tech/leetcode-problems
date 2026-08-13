class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        s=0
        for i in gain:
            s=s+i
            a.append(s)
        return max(a)
        

        