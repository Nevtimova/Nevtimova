n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

primary_sum = sum(matrix[i][i] for i in range(n))
secondary_sum = sum(matrix[i][n - i - 1] for i in range(n))

print(abs(primary_sum - secondary_sum))
