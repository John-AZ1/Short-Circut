from Empty import Empty
class tile2d:
    def __init__(self,x,y,obj=Empty(), id=0, point="*"):
        self.id = id
        self.x = x
        self.y = y
        self.containedSRadi = []
        self.obj = obj
        # Display Variables
        self.point = point
    def updateObj(self, obj):
        self.obj = obj
    def terrain(self):
        if self.obj.serial is "Empty":
            lT = ""
            for i in self.containedSRadi: lT+="{} "
            lT = "{a} "+lT
            return(lT.format(a=self.point, *self.containedSRadi))
        else:
            lT = ""
            for i in self.containedSRadi: lT+="{} "
            lT = "{a} {b}{c} "+lT
            return(lT.format(a=self.point, b=self.obj.serial, c=self.obj.id, *self.containedSRadi))
    def updateSRadi(self, sid, purge=False):
        if purge is True:
            self.containedSRadi = [x for x in self.containedSRadi if x != "S%d"%sid]
        else:
            self.containedSRadi = [x for x in self.containedSRadi if x != "S%d"%sid]
            self.containedSRadi.append("S%d"%sid)
        # print("tile2d: sRadi updated")
