def Extended_GCD(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = Extended_GCD(q % p, p)
        return (gcd, v - (q // p) * u, u)

p = 26513
q = 32321

gcd, u, v = Extended_GCD(p, q)
print("GCD= {}".format(gcd))
print("u,v= {},{}".format(u,v))