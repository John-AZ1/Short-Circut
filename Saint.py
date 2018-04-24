# Importing parent object
from Object import Object
# Creating Saint Object
class Saint(Object):
    def __init__(self, id, x, y):
        super().__init__(id, x, y, "no")
