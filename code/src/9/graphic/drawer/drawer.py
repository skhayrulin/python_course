import png

class Color:
    """Color class"""

    def __init__(self, r, g, b):
        """constructor

        :param r: red color component
        :param g: green color component
        :param b: blue color component
        """
        self.__r = r
        self.__g = g
        self.__b = b

    @property
    def r(self) -> int:
        """r color componenet"""
        return self.__r

    @property
    def g(self) -> int:
        """g color componenet"""
        return self.__g

    @property
    def b(self) -> int:
        """b color componenet"""
        return self.__b

    def as_list(self):
        """return color as list"""
        return [self.__r, self.__g, self.__b]

class Drawer:
    """Drawer"""

    def __init__(self, h, w, background=None):
        """constructor

        :param h: height of image
        :param w: height of image
        :param background: background color
        """
        self.__h = h
        self.__w = w
        self.__background = background or Color(0,0,0)
        self.__buffer = []

        for _ in range(self.__h):
            row = []
            for _ in range(self.__w):
                row = row + self.__background.as_list()

            self.__buffer.append(row)

    def put_pixel(self, x, y, c):
        """put pixel on scene

        :param x: x coordinate
        :param y: y coordinate
        :param c: c color
        """
        if 0 <= x < self.__h and 0 <= y < self.__w:
            self.__buffer[y][x * 3 + 0] = c.r
            self.__buffer[y][x * 3 + 1] = c.g
            self.__buffer[y][x * 3 + 2] = c.b

    def save(self):
        """Save scene in file"""
        with open('gradient.png', 'wb') as f:
            w = png.Writer(self.__w, self.__h, greyscale=False)
            w.write(f, self.__buffer)
