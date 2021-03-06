def solution(A):
    m = max(A)
    if m < 1:
        return 1
    if len(A) == 1:
        return 2 if A[0] == 1 else 1
    l = [0] * m
    for i in range(len(A)):
        if A[i] > 0:
            l[A[i] - 1] = 1
    for i in range(m):
        if l[i] == 0:
            return i + 1
    return i + 2
A = [1, 3, 6, 5, 4]
print(solution(A))
