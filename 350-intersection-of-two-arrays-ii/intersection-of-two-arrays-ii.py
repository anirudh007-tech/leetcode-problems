class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        w=[]
        for i in set(nums1):
            if i in nums2:
                a=min(nums1.count(i),nums2.count(i))
                w.extend([i]*a)
        return w

        