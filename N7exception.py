class myException(Exception):
    def __init__(self,aaa,bbb):
        self.a=aaa
        self.b=bbb
        print(self.a)
        print(self.b)
    def ccc(self):
        print(222)
raise myException(1,2)
raise ZeroDivisionError
