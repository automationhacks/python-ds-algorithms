def reverse(string):
    acc = ''
    for i in range(len(string) - 1, -1, -1):
        acc += string[i]
    return acc


def reverse_recursive(string):
    if len(string) == 1:
        return string
    else:
        return reverse_recursive(string[1:]) + string[0]


def test_reverse():
    assert reverse('gaurav') == 'varuag'
    assert reverse_recursive('gaurav') == 'varuag'
