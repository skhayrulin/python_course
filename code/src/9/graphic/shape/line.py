from .shape import Shape
from ..drawer import Color

class Line(Shape):
    line_counter = 0
    def __init__(self, start, end, drawer):
        Shape.__init__(self, drawer)
        self.start = start
        self.end = end
    
    @staticmethod
    def stat():
        Line.line_counter += 1
        print(f"{Line.line_counter} was created")

    def draw(self):
        """ Realization of Bresenham's algorithm for drawing lines
        """
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y

        sign_x = 1 if dx>0 else -1 if dx<0 else 0
        sign_y = 1 if dy>0 else -1 if dy<0 else 0

        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy

        x, y = self.start.x, self.start.y

        error, t = el/2, 0

        c = Color(255,255,255)
        self.drawer.put_pixel(x, y, c)
        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            self.drawer.put_pixel(x, y, c)
        