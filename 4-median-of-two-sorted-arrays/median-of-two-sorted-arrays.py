class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        q=len(nums1)
        if len(nums1)%2!=0:
            return(float(nums1[q//2]))
        else:
            m=(q-1)//2
            w=(nums1[m]+nums1[m+1])/2
            return(float(w))



        