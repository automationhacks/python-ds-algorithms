from tests.models.binary_tree import TreeNode


# root, left, right (+ab)
def pre_order(root):
    order = []

    def traverse(node):
        if node:
            order.append(node.val)
        else:
            return

        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return order


def test_given_binary_tree_then_pre_order_traversal_should_match():
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    assert pre_order(tree) == [1, 2, 3]


def test_given_empty_binary_tree_then_pre_order_traversal_should_be_empty():
    tree = TreeNode()

    assert pre_order(tree) == [0]


def test_given_single_root_in_binary_tree_then_pre_order_traversal_should_have_root():
    tree = TreeNode(1)

    assert pre_order(tree) == [1]


def test_given_only_left_child_in_binary_tree_then_pre_order_traversal_should_match():
    tree = TreeNode(1)
    tree.left = TreeNode(2)

    assert pre_order(tree) == [1, 2]


def test_given_only_right_child_in_binary_tree_then_pre_order_traversal_should_match():
    tree = TreeNode(1)
    tree.right = TreeNode(2)

    assert pre_order(tree) == [1, 2]
