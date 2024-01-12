from math import sqrt

def Dot_Product(v1, v2):
    return sum(a*b for a, b in zip(v1, v2)) # tương đương với a in v1 * b in v2

def Vector_Norm(v):
    return sqrt(Dot_Product(v, v))

Vectors = [[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]]

def gram_smith(Vectors):
    u = []
    for i in range(len(Vectors)):
        ui = Vectors[i]
        for j in range(i):
            muj = Dot_Product(Vectors[i], u[j]) / Vector_Norm(u[j])**2
            ui = [ui[k] - muj * u[j][k] for k in range(len(ui))]
        u.append(ui)
    return u

Flag = round(gram_smith(Vectors)[3][1],5)
print(Flag)