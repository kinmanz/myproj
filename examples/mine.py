


def method (a, n):
    p = 1
    x = a
    while n != 0:
        if n % 2 == 1:
            p *= x
        n = n // 2
        x *= x
    return p


print(method(3, 5))
