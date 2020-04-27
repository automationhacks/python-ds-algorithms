from data_structures.stack.stack import Stack


# To convert decimal to binary
# Take any no and divide by 2 till no is not 0
# Also push the remainder of this division on a stack
# When you pop the stack, you shall get your binary no

# We can repeat the same by making base generic (8 - octal, 16 - hex)
# Also have a mapping of hex nos such that nos > 9 and < 16 can be represented
# by ABCDEF and so on.

def base_converter(num, base):
    digits = '0123456789ABCDEF'
    stack = Stack()

    while num > 0:
        remainder = num % base
        stack.push(remainder)
        num = num // base

    binary_str = ""
    while not stack.is_empty():
        binary_str += digits[stack.pop()]

    return binary_str


assert base_converter(99, 2) == '1100011'
assert base_converter(26, 8) == '32'
assert base_converter(26, 16) == '1A'
