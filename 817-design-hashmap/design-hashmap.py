class MyHashMap:

    def __init__(self):
        self.lis=[]


    def put(self, key: int, value: int) -> None:
        k=1
        if self.lis==[]:
             a=[key,value]
             self.lis.append(a)
        for i in self.lis:
            if i[0]==key:
                k=0
                i[1]=value
                break
        if k==1:
            a=[key,value]
            self.lis.append(a)
            
        


    def get(self, key: int) -> int:
        for i in self.lis:
            if i[0]==key:
                return i[1]
        return -1


    def remove(self, key: int) -> None:
        k=-1
        for i in range(len(self.lis)):
            if self.lis[i][0]==key:
                k=i
        if k!=-1:
            self.lis.pop(k)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)