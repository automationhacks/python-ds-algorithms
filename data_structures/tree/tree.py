class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        if self.left_child:
            self._push_existing_left_node_down(node)
        else:
            self.left_child = BinaryTree(node)

    def _push_existing_left_node_down(self, node):
        temp = BinaryTree(node)
        temp.left_child = self.left_child
        self.left_child = temp

    def insert_right(self, node):
        if self.right_child:
            self._push_existing_right_node_down(node)
        else:
            self.right_child = BinaryTree(node)

    def _push_existing_right_node_down(self, node):
        temp = BinaryTree(node)
        temp.right_child = self.right_child
        self.right_child = temp

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root(self):
        return self.key

    def set_root(self, value):
        self.key = value


def test_binary_tree_is_created_with_nodes():
    root = BinaryTree('a')
    assert root.left_child is None
    assert root.right_child is None

    root.insert_left('b')
    assert root.get_left_child().get_root() == 'b'

    root.insert_right('c')
    assert root.get_right_child().get_root() == 'c'

    root.get_right_child().set_root('hello')
    assert root.get_right_child().get_root() == 'hello'
