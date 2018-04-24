from map2d import map2d
from tile2d import tile2d
from Empty import Empty
import Map
# Creating a parent class for all other objects to inherit.
# Objects (Implemented):
#   Saint
# Objects (Not Yet Impletmented):
#   Wall, Rock
class Object:
    def __init__(self, id, x, y, serial):
        self.id = id
        self.x = x
        self.y = y
        # Defines type
        self.serial = serial
        # Defines the search Radius
        self.searchR = 1
        self.sRadius = self.updateSRadius();
        # Adds self to Map.Map
        if type(Map.Map[x][y].obj) != Empty:
            print(Map[x][y].obj)
            print("Object Already Exists at (%d,%d). Cannot Initialize %s%d on Map" % (self.x, self.y, self.serial, self.id))
        else:
            Map.Map[self.x][self.y].updateObj(self)
    # A method to locate a target in the search Radius (sRadius)
    def updateSRadius(self):
        # Makes a Map (2d Array) the size of the search radius (searchR) filled with tile2d objects that are filled with Empty Objects
        sRadius = map2d(self.searchR*2+1,self.searchR*2+1, tile2d, True)
        # Fills Map (sRadius) with tiles (tile2d) from real Map (Map.Map)
        for i in range(self.searchR*-1, self.searchR+1):
            for ii in range(self.searchR*-1, self.searchR+1):
                try:
                    sRadius[i+self.searchR][ii+self.searchR] = Map.Map[self.x-i][self.y-ii]
                    Map.Map[self.x-i][self.y-ii].updateSRadi(self.id)
                    print("Executing ...")
                except IndexError:
                    sRadius[i+self.searchR][ii+self.searchR] = tile2d(None,None)
        return sRadius
    def locate(self, target):
        # Checks the search radius for the target (An Object)
        xx = self.searchR*-1 -1
        yy = self.searchR*-1 -1
        for i in self.sRadius:
            xx += 1
            yy = self.searchR*-1 -1
            for ii in i:
                yy += 1
                # print(ii.Object)
                if target is ii.obj:
                    # Return Found if target is in search radius (sRadius)
                    return "{}{} Found at ({},{})".format(target.serial, target.id, xx*-1+self.searchR*self.x, yy*-1+self.searchR*self.y)
        # If target is not in search radius (sRadius)
        return "Not Found"
    def upgrade(self,var, inc=1):
        if var is "searchR":
            self.searchR +=inc
    def move(self, direction, step=1):
        if direction == "up":
            Map.Map[self.x][self.y].updateObj(Empty())
            Map.Map[self.x][self.y-1].updateObj(self)
            Map.Map[self.x][self.y-1].updateSRadi(self.id)
            self.updateSRadius()
