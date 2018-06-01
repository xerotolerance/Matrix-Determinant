'''
@Author: XeroTolerance
@Date: 5-22-17
@Descripton: Recursive implementation of Co-factor formula 
                for computing the determinant of an n x n square matrix
'''

def tabulate(A):
    subs = [[row[:x] + row[x + 1:] for row in A[1:]] for x in range(len(A[0]))]
    det = 0
    sign = 1
    for i in range(len(A[0])):
        n_d = determinant(subs[i])
        det += sign * A[0][i] * n_d
        sign *= -1
    return det


def determinant(A):
    det=0
    if len(A) == 1:
        return A[0][0]
    elif len(A) == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    else:
        # show(A)
        # showCofactorsLiteral(A)
        # showCofactorsNumeric(A)
        det = tabulate(A)
    return det


def show(m):
    for x in m:
        print(x)
    print()


def showCofactorsLiteral(A):
    sign = 0
    for num in range(len(A[0])):
        if sign == 0:
            print("[", A[0][num], " * det(A[0][", num, "])]", sep="", end = "")
            sign = 1
        elif sign == 1:
            print(" + [", A[0][num], " * det(A[0][", num, "])]", sep="", end = "")
        else:
            print(" - [", A[0][num], " * det(A[0][", num, "])]", sep="", end = "")
            sign *= -1
    print()


def showCofactorsNumeric(A):
    subs = [[row[:x] + row[x + 1:] for row in A[1:]] for x in range(len(A[0]))]
    det = 0
    sign = 0
    for i in range(len(A[0])):
        n_d = determinant(subs[i])
        if sign == 0:
            print ("[", A[0][i], " * ", n_d, "]", sep="", end = "")
            sign = 1
        elif sign == -1:
            print (" - [", A[0][i], " * ", n_d, "]", sep="", end = "")
        else:
            print (" + [", A[0][i], " * ", n_d, "]", sep="", end = "")
        det += sign * A[0][i] * n_d
        sign *= -1
    print(" =", det)
