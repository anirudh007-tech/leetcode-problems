class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        if n<=999:
            return 0
        elif n>999:
            return n-999
       