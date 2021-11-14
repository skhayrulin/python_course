class Scene:
    def __init__(self, shapes):
        self.shapes = shapes

    def draw(self):
        for shape in self.shapes:
            shape.draw()