from abc import abstractmethod



class Shape:
    """Class Shape defines a interface for all gorahical primetives"""
    def __init__(self, drawer):
        self.drawer = drawer

        
    @abstractmethod
    def draw(self):
        # This is 
        pass