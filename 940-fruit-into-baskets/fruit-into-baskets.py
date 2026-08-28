class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a={}
        l=0
        m=0
        for i in range(len(fruits)):
            if fruits[i] in a:
                a[fruits[i]]+=1
            else:
                a[fruits[i]]=1
            if len(a)>2:
                a[fruits[l]]-=1
                if a[fruits[l]]==0:
                    del a[fruits[l]]
                l+=1
            m=max(m,i-l+1)
        return m


        




            
        