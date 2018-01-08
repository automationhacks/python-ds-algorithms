"""
Solution 3:
Anagram strings should have same no of characters
"""


def is_anagram(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')  # ord('a') = 97
        c1[pos] += 1  # Update count of character in array

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')  # ord('a') = 97
        c2[pos] += 1

    j = 0
    still_okay = True

    while j < 26 and still_okay:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_okay = False

    return still_okay

print(is_anagram('python', 'typhon'))


"""
Analysis:
Since there is no nesting and we have 2 loops which perform a linear time
Computation, T(n) = 2n + 26 where 26 is the 26 steps which we need to walk to 
compare the count

Thus its O(n)
"""
