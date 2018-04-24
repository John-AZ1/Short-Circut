l = ["0", "1", "2"]
lT = ""
for i in l: lT+="{} "
lT = "{a} "+lT
print(lT.format(a="Hi", *l))
