from map2d import map2d
from tile2d import tile2d
# Local Variables
x, y = 10, 10
Map = map2d(x,y, tile2d, True)
def printMap():
    for y in range(len(Map[0])):
        for x in range(len(Map)):
            print(Map[x][y].terrain(), end=" ")
            for g in range(15 - len(Map[x][y].terrain())):
                print(" ", end="")
        print("", end="\n")
