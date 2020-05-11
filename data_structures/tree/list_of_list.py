tree = [
    'a',
    ['b',
     ['d', [], []],
     ['e', [], []]
     ],
    ['c',
     ['f', [], []],
     []
     ],
]


def test_access_of_nodes():
    # Access root
    assert tree[0] == 'a'
    # Access left child
    assert tree[1] == ['b',
                       ['d', [], []],
                       ['e', [], []]
                       ]
    # Access right child
    assert tree[2] == ['c',
                       ['f', [], []],
                       []
                       ]


def binary_tree(root):
    return [root, [], []]


def insert_left(root, branch):
    # Push the current node down if not empty by making it left child
    # of the newly inserted branch
    node = root.pop(1)
    root.insert(1, [branch, node, []])


def insert_right(root, branch):
    node = root.pop(2)
    root.insert(2, [branch, [], node])


def get_root(root):
    return root[0]


def set_root(root, value):
    root[0] = value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def test_binary_tree_creation_using_classes():
    root = binary_tree(3)
    insert_left(root, 4)
    insert_left(root, 5)
    insert_right(root, 6)
    insert_right(root, 7)

    left = get_left_child(root)
    assert left[0] == 5
    set_root(left, 9)
    assert left[0] == 9

    insert_left(left, 11)
    assert root == [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
    assert get_right_child(get_right_child(root)) == [6, [], []]
