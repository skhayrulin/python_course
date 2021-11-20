class A:
    def __init__(self, x):
        self.x = x


if __name__ == '__main__':
    a = A(1)
    a.y = 2
    print(f"{a.x=} {a.y=}")
    b = A(2)
    print(f"{b.x=} {b.y=}")