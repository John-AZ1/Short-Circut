import Map
# Import Saint Object.
from Saint import Saint
# Objects and giving them id numbers (self.id) and Co-ordinates (self.x, self.y)
# co1 = input("Please enter co-ordinates for no1: ").split(" ")
# co2 = input("Please enter co-ordinates for no2: ").split(" ")
co1, co2 = [1,1], [1,2]
# co1 = input("Please enter co-ordinates for no1: ").split(" ")
no1 = Saint(1, int(co1[0]), int(co1[1]))
no2 = Saint(2, int(co2[0]), int(co2[1]))

# Main
no1.move("right")
no1.move("right")
no1.move("right")
no1.move("right")
no1.move("right")
no1.move("right")

no2.move("right")
no2.move("right")
no2.move("right")
no2.move("right")
no2.move("right")
print(no1.locate(no2))
Map.printMap()
