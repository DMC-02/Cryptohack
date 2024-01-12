def Chinese_Remainder_Theorem(congruences):
    N = 1
    for congruence in congruences:
        N *= congruence[1]

    result = 0
    for congruence in congruences:
        r, m = congruence

        i = N // m

        e = pow(i, -1, m)

        result += r * i * e

    return result % N

congruences = [(2,5), (3,11), (5,17)]

Flag = Chinese_Remainder_Theorem(congruences)
print(Flag)