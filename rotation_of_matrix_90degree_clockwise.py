def rotate90Clockwise(A):
    N = 4
    for j in range(N) :
        for i in range(N - 1, -1, -1) :
            print(A[i][j], end = " ")
        print()

A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
res= rotate90Clockwise(A)
print(res)
