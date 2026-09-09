import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            w=bisect_left(nums,target)
            t=bisect_right(nums,target)
            if w==t:
                return [-1,-1]
            else:
                return [w,t-1]
        
            
        