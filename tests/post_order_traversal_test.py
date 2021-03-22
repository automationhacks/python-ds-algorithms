from tests.models.binary_tree import TreeNode


# left, right, root (ab+)
def post_order(root):
    post_order = []

    def traverse(node):
        if not node:
            return

        traverse(node.left)
        traverse(node.right)
        post_order.append(node.val)

    traverse(root)
    return post_order


def test_given_binary_tree_then_post_order_traversal_should_match():
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    assert post_order(tree) == [3, 2, 1]


def test_given_empty_binary_tree_then_post_order_traversal_should_be_empty():
    tree = TreeNode()

    assert post_order(tree) == [0]


def test_given_single_root_in_binary_tree_then_post_order_traversal_should_have_root():
    tree = TreeNode(1)

    assert post_order(tree) == [1]


def test_given_only_left_child_in_binary_tree_then_post_order_traversal_should_match():
    tree = TreeNode(1)
    tree.left = TreeNode(2)

    assert post_order(tree) == [2, 1]


def test_given_only_right_child_in_binary_tree_then_post_order_traversal_should_match():
    tree = TreeNode(1)
    tree.right = TreeNode(2)

    assert post_order(tree) == [2, 1]
