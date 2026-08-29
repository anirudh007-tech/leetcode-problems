class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        m=[]
        r=len(height)-1
        while l<r:
            m.append((r-l)*min(height[l],height[r]))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return max(m)
            

        