import operator

from data_structures.stack.stack import Stack
from data_structures.tree.tree import BinaryTree

operator_map = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


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


def evaluate(parse_tree):
    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    # Recurse and call the operator on the return from recursion
    if left_child and right_child:
        func = operator_map[parse_tree.get_root()]
        return func(evaluate(left_child), evaluate(right_child))
    else:
        # Base case (If left, right child are None, then it must be a leaf)
        return parse_tree.get_root()


def test_parse_tree_create():
    p_tree = build_parse_tree('( ( 10 + 5 ) * 3 )')
    assert p_tree.get_root() == '*'
    assert evaluate(p_tree) == 45
