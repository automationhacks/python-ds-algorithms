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

    def __delitem__(self, key):
        self.delete(key)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError(f'<{key}> key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError(f'<{key}> key not in tree')

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node.parent.left_child == current_node:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.payload = successor.payload
        else:  # if node has one child
            # which is the left child
            if current_node.has_left_child():
                # Case 1: If current node has left child and
                # is the left child itself
                # Update reference in parent and left child such that
                # left child of current node becomes the new left child of
                # parent
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                # Case 2: If current node has a left child and is a right
                # child, then Replace left child as the right child of
                # parent
                # Update parent of left child to current nodes parent
                # Update parents right child to the current nodes left child
                elif current_node.is_right_child():

                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                # Case 3: Current node must be root, then replace current
                # left child node as the new root via replace_node_data
                else:
                    current_node.replace_node_data(
                        current_node.left_child.key,
                        current_node.left_child.payload,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child
                    )
            else:  # current node must have a right child
                # Case 1: If current node is a left child,
                # then set current node's right child's parent to current
                # nodes parent
                # and current nodes parent left child to the cur nodes
                # right child
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                # Case 2: If current node is a right child and has a right child
                # then replace parent to curr nodes parent
                # and parents right child to current nodes right child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                # Case 3: Current node must be root since it does not have
                # left or right child
                # Replace right child with root via replace_node_data
                else:
                    current_node.replace_node_data(
                        current_node.right_child.key,
                        current_node.right_child.payload,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )


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

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor
                    self.parent.right_child = self
        return successor

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    # Using in order traversal
    # for elem in (recursively calls __iter__ method
    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem


def test_binary_search_tree():
    bst = BinarySearchTree()

    bst[1] = 'Rob'
    bst[2] = 'Smith'
    bst[10] = 'Karl'

    assert bst[2] == 'Smith'
    assert 10 in bst


