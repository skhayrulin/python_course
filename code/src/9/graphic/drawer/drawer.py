import png

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def as_list(self):
        return [self.r, self.g, self.b]

class Drawer:
    def __init__(self, h, w, background=None):
        self.h = h
        self.w = w
        self.background = background or Color(0,0,0)
        self.__buffer = []

        for y in range(self.h):
            row = []
            for _ in range(self.w):
                row = row + self.background.as_list()

            self.__buffer.append(row)

    def put_pixel(self, x, y, c):
        self.__buffer[x][y * 3 + 0] = c.r
        self.__buffer[x][y * 3 + 1] = c.g
        self.__buffer[x][y * 3 + 2] = c.b

    def save(self):
        with open('gradient.png', 'wb') as f:
            w = png.Writer(self.w, self.h, greyscale=False)
            w.write(f, self.__buffer)

