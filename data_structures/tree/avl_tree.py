from data_structures.tree.binary_search_tree import BinarySearchTree, TreeNode


class AVLTreeNode(TreeNode):
    def __init__(self, key, val, left_child=None, right_child=None,
                 parent=None):
        self.balance_factor = 0
        super().__init__(key, val, left_child, right_child, parent)


class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = AVLTreeNode(key, value,
                                                      parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = AVLTreeNode(key, value,
                                                       parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return

        if node.parent:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def left_rotate(self, old_root):
        # Get a pointer to the new root (rchild of old)
        new_root = old_root.right_child

        # Update pointer of old root to any left child of new root
        old_root.right_child = new_root.left_child

        # If new had a left child, update that lchilds parent to old root
        if new_root.left_child:
            new_root.left_child.parent = old_root

        # Update new root to have same parent
        new_root.parent = old_root.parent

        # If the old was a root, update root
        # Else update the child link of old roots parent to point to the
        # new root
        if old_root.is_root():
            self.root = new_root
        else:
            if old_root.is_left_child():
                old_root.parent.left_child = new_root
            else:
                old_root.parent.right_child = new_root

        # Finally we update the links between the two nodes
        new_root.left_child = old_root
        old_root.parent = new_root

        old_root.balance_factor = old_root.balance_factor + 1 - min(
            new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(
            old_root.balance_factor, 0)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.right_rotate(node.right_child)

            self.left_rotate(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.left_rotate(node.left_child)

            self.right_rotate(node)
