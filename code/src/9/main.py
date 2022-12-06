import math

from graphic.drawer import Drawer, Color
from graphic.shape import Point2D, Line

def main():
    s = Scene()
    drawer = Drawer(256, 256)
    p_start = Point2D(100, 100, drawer=drawer)
    # p_end = Point2D(200, 200, drawer=drawer)
    for phi in [0, 45, 90, 135, 180, 225, 270, 315]:
        x = int(100 * math.cos(math.radians(phi)) + 100)
        y = int(100 * math.sin(math.radians(phi)) + 100)
        p_end = Point2D(x, y, drawer=drawer)
        l = Line(p_start, p_end, drawer)
        l.draw()
    drawer.save()

if __name__ == '__main__':
    main()