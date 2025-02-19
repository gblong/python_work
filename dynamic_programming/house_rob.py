def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]

def rob_opt(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev1, prev2 = 0, 0
    for num in nums:
        temp = prev1
        prev1 = max(prev1, prev2 + num)
        prev2 = temp

    return prev1

print(rob([2,7,9,3,1])) # 2+9+1
print(rob_opt([2,7,9,3,1])) # 2+9+1