class Base:
    def __init__(self, x, y):
        print("Run Base __init__ method")
        self.x = x
        self.y = y

class Other:
    def __init__(self, a, b):
        print("Run Other __init__ method")
        self.a = a
        self.b = b

class Children(Base, Other):
    def __init__(self, x, y, z):
        Base.__init__(self, x, y)
        Other.__init__(self, x, y)
        self.z = z
    
if __name__ == '__main__':
    c = Children(1, 2, 3)
    print(f"{c.x=} {c.y=} {c.z=} {c.a=} {c.b=}")