def Euclid_GCD(x, y):
    if x < y:
        return Euclid_GCD(y, x)

    while y != 0:
        (x, y) = (y, x % y)

    print("\nGCD= {}".format(x))
    return x

# a = 12
# b = 8

a = 66528
b = 52920

Euclid_GCD(a, b)