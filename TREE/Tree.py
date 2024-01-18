class Drzewo:

    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Drzewo(data))

    def remove(self, data):
        self.children = [child for child in self.children if child.data != data]

class Tree:

    def __init__(self):
        self.root = None

    def traverseBF(self, func):
        if not self.root:
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)
            func(current)
            queue.extend(current.children)


    def traverseDF(self, func):
        if not self.root:
            return

        stack = [self.root]

        while stack:
            current = stack.pop()
            func(current)
            stack.extend(reversed(current.children))
