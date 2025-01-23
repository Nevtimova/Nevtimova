rows, cols = map(int, input().split())

matrix = [[f"{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}" for c in range(cols)] for r in range(rows)]

for row in matrix:
    print(" ".join(row))
