import unittest

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


class TestDrzewo(unittest.TestCase):
    def test_constructor(self):
        n = Drzewo('a')
        self.assertEqual(n.data, 'a')
        self.assertEqual(len(n.children), 0)

    def test_add_children(self):
        n = Drzewo('a')
        n.add('b')
        self.assertEqual(len(n.children), 1)
        self.assertEqual(len(n.children[0].children), 0)

    def test_remove_children(self):
        n = Drzewo('a')
        n.add('b')
        self.assertEqual(len(n.children), 1)
        n.remove('b')
        self.assertEqual(len(n.children), 0)


class TestTree(unittest.TestCase):
    def test_starts_empty(self):
        t = Tree()
        self.assertIsNone(t.root)

    def test_traverse_bf(self):
        letters = []
        t = Tree()
        t.root = Drzewo('a')
        t.root.add('b')
        t.root.add('c')
        t.root.children[0].add('d')

        def traverse_callback(drzewo):
            letters.append(drzewo.data)

        t.traverseBF(traverse_callback)
        self.assertEqual(letters, ['a', 'b', 'c', 'd'])

    def test_traverse_df(self):
        letters = []
        t = Tree()
        t.root = Drzewo('a')
        t.root.add('b')
        t.root.add('d')
        t.root.children[0].add('c')

        def traverse_callback(drzewo):
            letters.append(drzewo.data)

        t.traverseDF(traverse_callback)
        self.assertEqual(letters, ['a', 'b', 'c', 'd'])


if Drzewo == '__main__':
    unittest.main()

