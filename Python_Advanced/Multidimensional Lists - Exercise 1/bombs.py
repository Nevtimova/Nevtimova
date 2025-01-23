n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

bombs = [tuple(map(int, coord.split(","))) for coord in input().split()]

def detonate_bomb(matrix, row, col):
    value = matrix[row][col]
    if value > 0:
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < n and 0 <= c < n and matrix[r][c] > 0:
                    matrix[r][c] -= value
        matrix[row][col] = 0

for bomb_row, bomb_col in bombs:
    detonate_bomb(matrix, bomb_row, bomb_col)

alive_cells = [cell for row in matrix for cell in row if cell > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    print(" ".join(map(str, row)))
