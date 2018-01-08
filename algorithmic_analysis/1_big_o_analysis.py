a = 5
b = 6
c = 10

for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j

for k in range(n):
    w = a * k + 45
    v = b * b

d = 33

"""
Algorithmic analysis:
Ln 1 to 3: constant : 3
Ln 5 to 9: 3 assignments for n^2 i.e. 3n^2
Ln 11 to 13: 2 assignments for n i.e. 2n
Ln 15: constant: 1

T(n) = 3 + 3n^2 + 2n + 1 = 4 + 3n^2 + 2n

Thus as value of n increases, its clear dominant part or f(n) would be
n^2. i.e. n square
"""
