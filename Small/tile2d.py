from Empty import Empty
class tile2d:
    def __init__(self,x,y,Object=Empty(), id=0, point="*"):
        self.id = id
        self.x = x
        self.y = y
        self.sRadi = []
        self.Object = Object
        # Display Variables
        self.point = point
        # if self.Object.serial is "Empty":
        #     self.terrain = "%s" % (self.point)
        # else:
        #     self.terrain = "%s %s%d" % (self.point, self.Object.serial, self.Object.id)s
        self.terrain = "%s %s%d" % (self.point, self.Object.serial, self.Object.id)
        # self.terrain = str(self.Object.id)
    def changeObj(self, obj):
        print("Executing ...")
        self.Object = obj
