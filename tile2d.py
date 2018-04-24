from Empty import Empty
class tile2d:
    def __init__(self,x,y,obj=Empty(), id=0, point="*"):
        self.id = id
        self.x = x
        self.y = y
        self.sRadi = []
        self.obj = obj
        # Display Variables
        self.point = point
    def updateObj(self, obj):
        self.obj = obj
    def terrain(self):
        if self.obj.serial is "Empty":
            lT = ""
            for i in self.sRadi: lT+="{} "
            lT = "{a} "+lT
            return(lT.format(a=self.point, *self.sRadi))
        else:
            lT = ""
            for i in self.sRadi: lT+="{} "
            lT = "{a} {b}{c} "+lT
            return(lT.format(a=self.point, b=self.obj.serial, c=self.obj.id, *self.sRadi))
    def updateSRadi(self, sid):
        self.sRadi = [x for x in self.sRadi if x != "S%d"%sid]
        self.sRadi.append("S%d"%sid)
