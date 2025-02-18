def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = grid[0][0]  # 起点

    # 初始化第一行
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # 初始化第一列
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # 计算 DP
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]


def min_path_sum_opt(grid):
    m, n = len(grid), len(grid[0])
    dp = [float('inf')] * n
    dp[0] = 0  # 初始状态

    for i in range(m):
        for j in range(n):
            if j == 0:
                dp[j] += grid[i][j]  # 第一列
            else:
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

    return dp[-1]

grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
print(min_path_sum(grid))
print(min_path_sum_opt(grid))