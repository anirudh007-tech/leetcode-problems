class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       a={} 
       for i,n in enumerate(nums):
        if n in a and i-a[n]<=k:
            return True
        a[n]=i
       return False
                    
                
        
            


        
        