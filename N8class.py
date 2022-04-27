class Apple:
    name="xxx"
    def fun1(self):
        return 'normal'
    @staticmethod
    def fun2():
        return 'staticmethod'
    @classmethod
    def fun3(cls):
        return 'classmethod'
print(id(Apple.name))
print(id(Apple))
print(id(Apple.fun1))
print(id(Apple.fun2))
print(id(Apple.fun3))
print(Apple.name)
print(Apple.fun1)
print(Apple.fun2())
print(Apple.fun3())
print("-"*80)
apple = Apple()
print(apple.fun1)
print(apple.fun2)
print(apple.fun3)
print("-"*80)
apple1 = Apple()
print(apple1.fun1)
print(apple1.fun2)
print(apple1.fun3)