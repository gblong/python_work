#动态规划 - 自底向上
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 金额为 0 时不需要任何硬币

    # 二重循环：遍历所有金额, 遍历所有硬币币值
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                #dp[i] = min(dp[i], dp[i - coin] + 1)
                min = dp[i - coin] + 1
                if min < dp[i]:
                    dp[i] = min

    return dp[amount] if dp[amount] != float('inf') else -1 # 三目运算符

# 示例
coins = [2,3,4]
amount = 5
print(coin_change_dp(coins, amount))  

#递归（自顶向下）+ 缓存 
def coin_change_recursive(coins, amount):
    cache = {}

    def dfs(rem):
        if rem == 0:
            return 0
        if rem < 0:
            return float('inf')

        # if rem in cache:
        #     return cache[rem]

        ret = min(dfs(rem - coin) + 1 for coin in coins)
        #cache[rem] = ret
        return ret

    res = dfs(amount)
    return res if res != float('inf') else -1


def dfs(rem):
        if rem == 0:
            return 0
        if rem < 0:
            return float('inf')

        # if rem in cache:
        #     return cache[rem]

        ret = min(dfs(rem - coin) + 1 for coin in coins)
        #cache[rem] = ret
        return ret

print(coin_change_recursive(coins, amount))  # 输出: 3