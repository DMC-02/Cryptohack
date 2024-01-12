import math

v = (4, 6, 2, 5)

Size = math.sqrt(sum(component ** 2 for component in v))

print(Size)