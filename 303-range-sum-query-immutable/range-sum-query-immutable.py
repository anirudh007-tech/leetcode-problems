class NumArray:

    def __init__(self, nums: List[int]):
        self.q=nums
        

    def sumRange(self, left: int, right: int) -> int:
        s=0
        a=[]
        for i in self.q:
            s=s+i
            a.append(s)
        if left==0:
            return a[right]
        else:
            return(a[right]-a[left-1])

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)