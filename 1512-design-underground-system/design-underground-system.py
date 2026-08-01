class UndergroundSystem:

    def __init__(self):
        self.c={}
        self.t={}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.c[id]=(stationName,t)

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        sta,ta=self.c.pop(id)

        time=abs(t-ta)
        q=(sta,stationName)
        if q in self.t:
            self.t[q][0]+=time
            self.t[q][1]+=1
        else:
            self.t[q]=[time,1]
        


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tr=(startStation,endStation)
        return self.t[tr][0] / self.t[tr][1]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)