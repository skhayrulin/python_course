class A:
    def __init__(self, a, b, c):
        self.public_atribute = a
        self._protected_field = b
        self.__private_field = c

if __name__ == '__main__':
    a = A(1, 2, 3)
    print(f"{a.public_atribute=} {a._protected_field=} {a.__private_field=}")
