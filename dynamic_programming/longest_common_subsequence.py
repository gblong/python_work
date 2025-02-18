def longest_common_subsequence(text1: str, text2: str) -> str:
    m, n = len(text1), len(text2) # 
    dp = [[0] * (n + 1) for _ in range(m + 1)] #matrix (m+1) 行 (n+1) 列
    backtrack = [[0] * (n + 1) for _ in range(m + 1)]
    LEFTUP, LEFT, UP = 0, 1, 2 #track flags:
    
    # 填充 dp 数组
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                backtrack[i][j] = LEFTUP
            elif dp[i - 1][j] >  dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                backtrack[i][j] = UP
            else:
                dp[i][j] = dp[i][j - 1]
                backtrack[i][j] = LEFT
    
    # 逆向构造最长公共子序列
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if backtrack[i][j] == LEFTUP:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif backtrack[i][j] == UP:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

# 示例
text1 = "1a2b3c4d5e6f7g"
text2 = "2a3b4c5d6789"
print(longest_common_subsequence(text1, text2))
