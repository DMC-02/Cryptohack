def Matrix_to_Bytes(matrix):
    arr = [chr(i) for j in matrix for i in j]
    Flag = ""
    for i in arr:
        Flag += i
    return Flag