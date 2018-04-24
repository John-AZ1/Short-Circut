import Map
# Import Saint Object.
from Saint import Saint
# Objects and giving them id numbers (self.id) and Co-ordinates (self.x, self.y)
# co1 = input("Please enter co-ordinates for no1: ").split(" ")
# co2 = input("Please enter co-ordinates for no2: ").split(" ")
co1, co2 = [0,0], [5,9]
# co1 = input("Please enter co-ordinates for no1: ").split(" ")
no1 = Saint(1, int(co1[0]), int(co1[1]))
no2 = Saint(2, int(co2[0]), int(co2[1]))
# Troubleshooting
print(no2.locate(no1))
# print(no1.locate(no2))
Map.printMap()
no2.move("up")
Map.printMap()
