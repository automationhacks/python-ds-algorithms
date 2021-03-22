from tests.models.binary_tree import TreeNode


# left, root, right (a+b)
def in_order(root):
    in_order = []

    def traverse(node):
        # base case:
        # if node is a leaf i.e. None, then you return
        if not node:
            return

        # left, root, right
        traverse(node.left)
        in_order.append(node.val)
        traverse(node.right)

    traverse(root)
    return in_order


def test_given_binary_tree_then_in_order_traversal_should_match():
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    assert in_order(tree) == [1, 3, 2]


def test_given_empty_binary_tree_then_in_order_traversal_should_be_empty():
    tree = TreeNode()

    assert in_order(tree) == [0]


def test_given_single_root_in_binary_tree_then_in_order_traversal_should_have_root():
    tree = TreeNode(1)

    assert in_order(tree) == [1]


def test_given_only_left_child_in_binary_tree_then_in_order_traversal_should_match():
    tree = TreeNode(1)
    tree.left = TreeNode(2)

    assert in_order(tree) == [2, 1]


def test_given_only_right_child_in_binary_tree_then_in_order_traversal_should_match():
    tree = TreeNode(1)
    tree.right = TreeNode(2)

    assert in_order(tree) == [1, 2]
