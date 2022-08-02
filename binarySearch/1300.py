import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

A_matrix = []

for i in range(1, N + 1):
    A_matrix.append(i ** 2)

    if i == 1:
        A_matrix.append(i)
    else:
        A_matrix.append(i)
        A_matrix.append(i)

    if i == N:
        A_matrix.append(i * (i - 1))
        A_matrix.append(i * (i - 1))

A_matrix = sorted(A_matrix)
print(A_matrix[K])
