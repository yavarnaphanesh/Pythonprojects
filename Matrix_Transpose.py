M = int(input())
N = int(input())
matrix = []

for _ in range(M):
    matrix_input = [int(x) for x in input(). split()]
    matrix . append(matrix_input)

list_of_sum = []
list_of_index = []

for i in range(M):
    sum = 0
    for j in range(N):
        sum += matrix[j][i]
    list_of_sum.append(sum)
max_value = max(list_of_sum)

max_indices = [i+1 for i, x in enumerate(list_of_sum) if x == max_value]

print(max_indices)
