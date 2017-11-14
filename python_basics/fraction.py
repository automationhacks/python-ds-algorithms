"""
Implement a fraction class, able to represent numerator / denominator.
It should have methods to perform add, sub, mul and division
"""


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        """
        Override default impl to convert object to string,
        If not, default __str__ impl would print the objects address
        """
        return '{} / {}'.format(self.num, self.den)

    def __add__(self, other_fraction):
        """
        We can add two fractions if they have common num and den:
        i.e.
            a   c   ab  cb      ac + cb
            - + - =  - + -  =   -------
            b   d   bd  bd         bd
        """
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = self.gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def gcd(self, m, n):
        """
        GCD (Greatest common divisor) of m or n is if n divides m evenly
        if it does not divide evenly then,
        Greatest of common divisor of n and remainder of m divided by n
        """
        while m % n != 0:
            old_m, old_n = m, n
            m, n = old_n, old_m % old_n
        return n



# myf = Fraction(3, 5)
# print(myf)
# print(myf.__str__())

# f1 = Fraction(1, 4)
# f2 = Fraction(1, 2)
# print(f1 + f2)

# Above would result in exception as:
# since '+' operator does not understand fraction operands.
# Traceback (most recent call last):
#   File "fraction.py", line 26, in <module>
#     print(f1 + f2)
# TypeError: unsupported operand type(s) for +: 'instance' and 'instance'

# After implementation of __add__

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)

