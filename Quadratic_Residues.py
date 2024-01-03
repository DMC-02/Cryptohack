p = 29
ints = [14, 6, 11]

def Quadratic_Residue_Find(p, ints):
    Quadratic_residue = None

    for a in range(1, p):
        if (a**2) % p in ints:
            Quadratic_residue = (a**2) %p
            break
        return Quadratic_residue
    
def Calculate_Square_Root(p, Quadratic_Residue):
    a=1
    while (a**2) %p != Quadratic_Residue:
        a+=1
    return a

Quadratic_residue = Quadratic_Residue_Find(p, ints)
Square_root=Calculate_Square_Root(p, Quadratic_residue)

print(Square_root)