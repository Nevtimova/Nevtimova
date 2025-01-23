n = int(input())

commands = input().split()

field = []
miner_row, miner_col = 0, 0
total_coal = 0

for row in range(n):
    line = input().split()
    field.append(line)
    if "s" in line:
        miner_row, miner_col = row, line.index("s")
    total_coal += line.count("c")

for command in commands:
    if command == "up" and miner_row > 0:
        miner_row -= 1
    elif command == "down" and miner_row < n - 1:
        miner_row += 1
    elif command == "left" and miner_col > 0:
        miner_col -= 1
    elif command == "right" and miner_col < n - 1:
        miner_col += 1

    if field[miner_row][miner_col] == "c":
        total_coal -= 1
        field[miner_row][miner_col] = "*"
        if total_coal == 0:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            break
    elif field[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        break
else:
    print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_col})")
