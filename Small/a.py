import tile2d
Map = [[tile2d.tile2d(w,h) for h in range(3)] for w in range(4)]
def printMap():
    for y in range(len(Map[0])):
        for x in range(len(Map)):
            print(Map[x][y].Object.terrain, end=" ")
            for g in range(5 - len(Map[x][y].terrain)):
                print(" ", end="")
        print("", end="\n")
# class notEmpty:
#     def __init__(self):
#         self.id = 1
#         self.serial = "Full"
#         self.x = 0
#         self.y = 0
#         self.terrain = "* Full1"
#         Map[self.x][self.y].changeObj(self)
# thing = notEmpty()
# printMap()
