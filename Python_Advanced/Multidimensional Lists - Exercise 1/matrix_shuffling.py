rows, cols = map(int, input().split())

matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()
    if (len(parts) == 5 and parts[0] == "swap" and
            all(part.isdigit() for part in parts[1:])):
        r1, c1, r2, c2 = map(int, parts[1:])
        if 0 <= r1 < rows and 0 <= c1 < cols and 0 <= r2 < rows and 0 <= c2 < cols:
            # Perform the swap
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for row in matrix:
                print(" ".join(row))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
