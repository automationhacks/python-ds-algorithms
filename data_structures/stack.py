# Python impl for a stack
# Uses a list to represent the stack


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


# Matching parenthesis problem
# https://www.youtube.com/watch?v=w6rusGR9oic&list=PLtbC5OfOR8aqfexTOHSzvdQhfCzp0mZ64&index=3

def is_balanced(expr):
    stack = Stack()

    for elem in expr:
        if elem in '({[<':
            stack.push(elem)
        else:
            if stack.is_empty():
                return False
            else:
                top = stack.pop()
                if top != symbol_map[elem]:
                    return False

    if stack.is_empty():
        return True
    else:
        return False


symbol_map = {
    ')': '(',
    '}': '{',
    '>': '<',
    ']': '[',
}


def test_valid_expression():
    expression = '(())()'
    assert is_balanced(expression)


def test_invalid_expression():
    expression = '()())()'
    assert not is_balanced(expression)


def test_valid_expression_for_all_symbols():
    expression = '<>{}[]()>'
    assert is_balanced(expression)


if __name__ == '__main__':
    test_valid_expression()
    test_invalid_expression()
    test_valid_expression_for_all_symbols()
