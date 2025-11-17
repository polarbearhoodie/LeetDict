import math


# arr_in can be NON-SQUARE
def rotate90(arr_in):
    n = len(arr_in)
    m = len(arr_in[0])
    arr_out = [[0 for i in range(n)] for j in range(m)]

    # the first row becomes the last column
    for i in range(n):
        for j in range(m):
            x = j
            y = (n-1) - i
            arr_out[x][y] = arr_in[i][j]

    return arr_out


# rotate across diagonal where i == j
def flip_cross(arr_in):
    n = len(arr_in)
    for i in range(n):
        for j in range(i, n):
            a = arr_in[i][j]
            b = arr_in[j][i]
            arr_in[i][j] = b
            arr_in[j][i] = a


# rotate across vertical split
def cross(arr_in):
    n = len(arr_in)
    for i in range(n):
        half = math.floor(n/2)
        for j in range(half):
            a = arr_in[i][j]
            b = arr_in[i][n-1-j]
            arr_in[i][j] = b
            arr_in[i][n-1-j] = a


# arr_in is SQUARE
# modify in-place, constant memory
def rotate450(arr_in):
    flip_cross(arr_in)
    cross(arr_in)
