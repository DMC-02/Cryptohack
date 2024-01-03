p = 29
ints = [14, 6, 11]

def Find_Quadratic_Residue(p, ints):
    Quadratic_Residue = None
    for a in range(1, p):
        if (a**2) % p in ints:
            Quadratic_Residue = (a**2) % p
            break
    return Quadratic_Residue

def Calculate_Square_Root(p, Quadratic_Residue):
    a = 1
    while (a**2) % p != Quadratic_Residue:
        a += 1
    return a

Quadratic_Residue = Find_Quadratic_Residue(p, ints)
square_Root = Calculate_Square_Root(p, Quadratic_Residue)

print(square_Root)