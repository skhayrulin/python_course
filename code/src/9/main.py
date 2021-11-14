from graphic.drawer import Drawer, Color
from graphic.shape import Point2D, Line

def main():
    drawer = Drawer(256, 256)
    p_start = Point2D(100, 100, drawer=drawer)
    p_end = Point2D(200, 200, drawer=drawer)
    l = Line(p_start, p_end, drawer)
    l.draw()
    drawer.save()

if __name__ == '__main__':
    main()