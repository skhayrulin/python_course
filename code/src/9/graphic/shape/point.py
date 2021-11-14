from .shape import Shape
from ..drawer import Color

class Point2D(Shape):
    description = "This is definition of 2D point"

    def __init__(self, x, y, drawer):
        Shape.__init__(self,drawer)
        self.x = x
        self.y = y

    def draw(self):
        self.drawer.put_pixel(self.x, self.y, Color(255,255,255))

class Point3D(Point2D):
    def __init__(self, x, y, z, drawer):
        super().__init__(x, y, drawer)
        self.z = z
    
    def draw(self):
        pass