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
