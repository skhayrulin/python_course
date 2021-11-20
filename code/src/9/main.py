import random

from graphic.scene import Scene
from graphic.drawer import Drawer, Color
from graphic.shape import Point2D, Line

def main():
    s = Scene()
    drawer = Drawer(256, 256)
    for _ in range(30):
        p_start = Point2D(random.randint(0, 255), random.randint(0, 255), drawer=drawer)
        p_end = Point2D(random.randint(0, 255), random.randint(0, 255), drawer=drawer)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        s.add(Line(p_start, p_end, drawer, color=Color(r,g,b)))
    s.draw()

    drawer.save()

if __name__ == '__main__':
    main()