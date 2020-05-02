"""
Write a function that takes a string as a parameter and returns True if
the string is a palindrome, False otherwise.
Remember that a string is a palindrome if it is spelled the same both
forward and backward. For example: radar is a palindrome.
for bonus points palindromes can also be phrases, but you need to
remove the spaces and punctuation before checking.
for example: madam i’m adam is a palindrome. Other fun palindromes include:

kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota
"""


def is_palindrome(string):
    first = 0
    last = len(string) - 1

    while first <= last:
        if string[first] != string[last]:
            return False
        else:
            first += 1
            last -= 1

    return True


def test_palindrome():
    assert is_palindrome('kayak')
    assert is_palindrome('aibohphobia')
