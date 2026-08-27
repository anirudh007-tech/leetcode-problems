# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=0
        right=n
        while left<=right:
            mind=(left+right)//2
            if isBadVersion(mind):
                right=mind-1
            else:
                left=mind+1
        return left

        