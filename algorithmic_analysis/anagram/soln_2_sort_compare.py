"""
Soln 2:

If two strings are sorted,
they should be anagram if each character position matches
in the sorted strings
"""


def is_anagram(s1, s2):
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    pos = 0
    matches = True

    while pos < len(list1) and matches:
        if list1[pos] == list2[pos]:
            pos += 1
        else:
            matches = False

    return matches

print(is_anagram('python', 'typhon'))

"""
Analysis:

Initially it might appear that algo is O(n)
however sorting is typically O(n^2) or O(n log n)
Thus this has the same complexity as solution 1 with list iteration

Here we added the values in two lists, thus sacrificing space to gain time
This is often the case and the programmer needs to to optimize for the scenario
In case the no of chars are in millions, this might not be a good approach
"""
