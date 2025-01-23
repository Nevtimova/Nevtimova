rows, cols = map(int, input().split())

snake = input()

matrix = []
snake_index = 0

for row in range(rows):
    current_row = []
    for col in range(cols):
        current_row.append(snake[snake_index])
        snake_index = (snake_index + 1) % len(snake)
    if row % 2 == 1:  # Reverse every second row
        current_row.reverse()
    matrix.append(current_row)

for row in matrix:
    print("".join(row))
