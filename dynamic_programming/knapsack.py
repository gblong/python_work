''''
动态规划解法
1. 定义状态
设 dp[i][j] 表示前 i 件物品在容量为 j 的背包中能获得的最大价值。

2. 状态转移方程
对于第 i 件物品，有两种选择：
不放入背包: dp[i][j] = dp[i-1][j]。
放入背包: dp[i][j] = dp[i-1][j-w[i]] + v[i]（前提是 j >= w[i]）。
因此，状态转移方程为：
dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

3. 初始化
dp[0][j] = 0: 没有物品时，最大价值为 0。
dp[i][0] = 0: 背包容量为 0 时，最大价值为 0。

4. 最终结果
dp[n][C] 即为所求的最大价值。
'''
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if j >= weights[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]

C = 5  # 背包容量
weights = [2, 1, 3, 2]  # 物品重量
values = [3, 2, 4, 2]   # 物品价值
print(knapsack(weights, values, C))
