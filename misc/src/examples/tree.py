"""
Simple tree struct.
"""

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.chldrn = []

    def show(self):
        return 'Node name {0}, Node value {1}, chldrn {2}'.format(self.name, self.value, self.chldrn)

class Tree:
    def __init__(self,root=None):
        if root:
            self.root = root
        else:
            self.root = Node('Root', 0)

    def visit(self):
        """
        Use DFS or BFS for visit all nodes of tree.
        """
        pass

    def show_tree(self):
        print(self.root.show())


def main():
    tree = Tree()
    tree.show_tree()

if __name__ == '__main__':
    main()
