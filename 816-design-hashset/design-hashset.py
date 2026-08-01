class MyHashSet:

    def __init__(self):
        self.i=[]
        

    def add(self, key: int) -> None:
        self.i.append(key)
        

    def remove(self, key: int) -> None:
        for j in self.i:
            if j==key:
                self.i.remove(key)
        
        

    def contains(self, key: int) -> bool:
        x=0
        for i in self.i:
            if i==key:
                x=1
        if x==1:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)