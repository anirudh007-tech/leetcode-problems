class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i!='#':
                a.append(i)
            else:
                if not a:
                    continue
                else:
                    a.pop()
        for i in t:
            if i!='#':
                b.append(i)
            else:
                if not b:
                    continue
                else:
                    b.pop()
        if a==b:
            return True
        else:
            return False 
     
    
        