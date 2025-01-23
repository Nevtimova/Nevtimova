rows, cols = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(rows)]

max_sum = float('-inf')
best_submatrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        current_submatrix = [matrix[row][col:col + 3],
                             matrix[row + 1][col:col + 3],
                             matrix[row + 2][col:col + 3]]
        current_sum = sum(sum(row) for row in current_submatrix)
        if current_sum > max_sum:
            max_sum = current_sum
            best_submatrix = current_submatrix

print(f"Sum = {max_sum}")
for row in best_submatrix:
    print(" ".join(map(str, row)))
