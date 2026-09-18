class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if not a:
                a.append(i)
            else:
                if a[-1]=='(' and i==')':
                    a.pop()
                elif a[-1]=='{' and i=='}':
                    a.pop()
                elif a[-1]=='[' and i==']':
                    a.pop()
                else:
                    a.append(i)
        if not a:
            return True
        else:
            return False

        