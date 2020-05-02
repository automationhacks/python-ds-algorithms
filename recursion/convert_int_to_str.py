# Reference: https://runestone.academy/runestone/books/published/pythonds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html

# if num < base (2, 8, 10, 16) then we can directly lookup the corresponding
# string value
# hence base case = if num < base then lookup
# To reduce the problem towards base case, we divide the no by base to get
# remaining nos i.e 769 // 10 = 76 and call the function recursively with the
# reduced no, Also we get the remainder via 769 % 10 = 9
# since remainder is always going to be less than 10, we directly lookup
# Finally we concatenate the two


def to_str(num, base):
    convert_string = '0123456789ABCDEF'

    if num < base:
        return convert_string[num]
    else:
        digit = num // base
        remainder = num % base
        return to_str(digit, base) + convert_string[remainder]


def test_base_convertor():
    assert to_str(10, 2) == '1010'
    assert to_str(769, 10) == '769'
    assert to_str(99, 2) == '1100011'
    assert to_str(26, 8) == '32'
    assert to_str(26, 16) == '1A'
