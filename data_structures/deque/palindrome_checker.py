from data_structures.deque.Deque import Deque


def is_palindrome(string):
    if not isinstance(string, str):
        return False

    deque = Deque()

    # O(n)
    for ch in string:
        deque.add_front(ch)

    # O(1) + O(n)
    while deque.size() > 1:
        front = deque.remove_front().lower()
        rear = deque.remove_rear().lower()
        if front != rear:
            return False

    return True
    # Overall: O(1) + 2 * O(n) = O(n)


def test_valid_palindrome():
    assert is_palindrome('racecar')


def test_empty_string():
    assert is_palindrome('')


def test_mixed_case():
    assert is_palindrome('RAcecar')


def test_single_char_string():
    assert is_palindrome('a')


def test_invalid_palidrome():
    assert not is_palindrome('gaurav')


def test_invalid_type():
    assert not is_palindrome(123)
