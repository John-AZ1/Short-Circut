import a
class notEmpty:
    def __init__(self):
        self.id = 1
        self.serial = "Full"
        self.x = 0
        self.y = 0
        self.terrain = "* Full1"
        a.Map[self.x][self.y].changeObj(self)
