class IWorker:
    def work(self):
        raise NotImplementedError("This interface so it doesn't do any work")
    
    def get_break(self):
        raise NotImplementedError("This interface so it doesn't do any work")


class CEO(IWorker):
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"CEO {self.name} is doing some realy important work.")    
    
    def get_break(self):
        print(f"CEO {self.name} tired so get rest.")    

class Coder(IWorker):
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"Coder {self.name} is writing a lot of code.")    

    def get_break(self):
        print(f"Coder {self.name} tired so get rest.")
