class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def put(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._put(key, value, self.root)

        self.size += 1

    def _put(self, key, value, current_node):
        # BST property, check if key to be added > current nodes key
        # Then check apt left or right subtree if they have children
        # Recurse if yes, else install the TreeNode and add reference to parent
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value,
                                                   parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value,
                                                    parent=current_node)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return True if self.get(item) else False

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)


class TreeNode:
    def __init__(self, key, val, left_child=None, right_child=None,
                 parent=None):
        self.key = key
        self.payload = val
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.payload = value
        self.left_child = left_child
        self.right_child = right_child

        if self.has_left_child():
            self.left_child.parent = self

        if self.has_right_child():
            self.right_child.parent = self


def test_binary_search_tree():
    bst = BinarySearchTree()

    bst[1] = 'Rob'
    bst[2] = 'Smith'
    bst[10] = 'Karl'

    assert bst[2] == 'Smith'
    assert 10 in bst
