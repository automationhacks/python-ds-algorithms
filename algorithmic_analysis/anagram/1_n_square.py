"""
Write a boolean function that takes two strings and returns if they
are anagrams

Example: python, typhon or earth, heart

Assumption:
1. strings would be made from english lowercase characters (26)
2. strings would be equal length
"""


# Solution 1:
# Find if each char in list 1 in present in list 2
# if found then update the value to None
# else if not found then ext out of the loop


def is_anagram(s1, s2):
    a_list = list(s2)

    pos_1 = 0
    still_ok = True

    while pos_1 < len(s1) and still_ok:
        pos_2 = 0
        found = False

        while pos_2 < len(a_list) and not found:

            if s1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 += 1

        if found:
            a_list[pos_2] = None
        else:
            still_ok = False

        pos_1 += 1

        return still_ok


print(is_anagram('python', 'typhon'))

"""
To analyze this algorithm, 
we need to note that each of the n characters in s1,
 will cause an iteration through up to n characters in the list from s2.
 Each of the n positions in the list will be visited once to match a character
 from s1. 
 The number of visits then becomes the sum of the integers from 1 to n.
 We stated earlier that this can be written as

n(n+1)/2 i.e. n^2/2 + n/2
As n gets large, the n^2 term will dominate the nn term
and the n/2 can be ignored. Therefore, this solution is O(n^2)
"""
