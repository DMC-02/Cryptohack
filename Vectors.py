v = (2,6,3)
w = (1,0,0)
u = (7,7,2)

def Vector_Minus(a,b):
    return [x - y for x, y in zip(a,b)]

def Vector_Dot(a,b):
    return sum([x*y for x, y in zip(a,b)])

def Scalar_Time(a, times):
    return list(map(lambda x: x * times, a))

print (Vector_Dot(Scalar_Time(Vector_Minus(Scalar_Time(v, 2),w), 3), Scalar_Time(u,2)))