class noNeg(list):
    def __getitem__(self,n):
        if n < 0:
            raise IndexError("...")
        return list.__getitem__(self, n)
class map2d(noNeg):
    def __init__(self,x,y, fill=None, fillc = False):
        for w in range(x):
            r = noNeg([])
            self.append(r)
            for h in range(y):
                if fillc == True:
                    r.append(fill(w,h))
                else:
                    r.append(fill)
