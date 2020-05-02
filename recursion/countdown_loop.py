def count_down(num):
    while num > 0:
        print(num, end=' ')
        num -= 1


def count_down_recursive(num):
    print(num, end=' ')
    if num > 1:
        count_down_recursive(num - 1)


print('With iteration')
count_down(10)
print()
print('With recursion')
count_down_recursive(10)
