from data_structures.stack.stack import Stack
from data_structures.tree.tree import BinaryTree

OPERATORS = ['+', '-', '*', '/']


def build_parse_tree(expr):
    tokens = expr.split()
    stack = Stack()

    tree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for token in tokens:
        if token == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        # If token is an operand (e.g. a number)
        elif token not in ['+', '-', '*', '/', ')']:
            try:
                current_tree.set_root(int(token))
                parent = stack.pop()
                current_tree = parent
            except ValueError:
                raise ValueError(f'Token {token} is not a valid integer')
        elif token in ['+', '-', '*', '/']:
            current_tree.set_root(token)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif token == ')':
            current_tree = stack.pop()

    return tree


def test_parse_tree_create():
    p_tree = build_parse_tree('( ( 10 + 5 ) * 3 )')
    assert p_tree.get_root() == '*'
