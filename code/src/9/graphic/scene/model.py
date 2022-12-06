class Scene:
    def __init__(self, shapes = None):
        self.__shapes = shapes or []

    def add(self, new_shape):
        self.__shapes.append(new_shape)
        
    def draw(self):
        for shape in self.__shapes:
            shape.draw()