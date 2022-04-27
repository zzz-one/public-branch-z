def c1():
    pass
def c2():
    print("2222")
    pass
for i in dir():
    if i.find("c",0,1)!=-1:
        eval(i)()