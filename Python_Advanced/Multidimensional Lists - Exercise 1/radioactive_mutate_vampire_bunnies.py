rows, cols = map(int, input().split())

lair = []
player_row, player_col = 0, 0
for row in range(rows):
    line = list(input())
    lair.append(line)
    if "P" in line:
        player_row, player_col = row, line.index("P")

moves = input()

def spread_bunnies(lair):
    new_lair = [row[:] for row in lair]
    for row in range(rows):
        for col in range(cols):
            if lair[row][col] == "B":
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        new_lair[nr][nc] = "B"
    return new_lair

for move in moves:
    lair[player_row][player_col] = "."
    if move == "U":
        player_row -= 1
    elif move == "D":
        player_row += 1
    elif move == "L":
        player_col -= 1
    elif move == "R":
        player_col += 1

    if not (0 <= player_row < rows and 0 <= player_col < cols):
        lair = spread_bunnies(lair)
        for row in lair:
            print("".join(row))
        print(f"won: {player_row} {player_col}")
        break

    lair = spread_bunnies(lair)

    if lair[player_row][player_col] == "B":
        for row in lair:
            print("".join(row))
        print(f"dead: {player_row} {player_col}")
        break

    lair[player_row][player_col] = "P"

else:
    for row in lair:
        print("".join(row))
    print(f"dead: {player_row} {player_col}")
