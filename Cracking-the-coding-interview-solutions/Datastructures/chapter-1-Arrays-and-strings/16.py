def rotate(matrix, degree):
    if abs(degree) not in [0, 90, 180, 270, 360]:
        # raise error or just return nothing or original
    if degree == 0:
        return matrix
    elif degree > 0:
        return rotate(zip(*matrix[::-1]), degree-90)
    else:
        return rotate(zip(*matrix)[::-1], degree+90)

matr_= [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print (matr_, 180)