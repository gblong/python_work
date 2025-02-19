#给定一个整数数组 nums，找到其中 最长递增子序列 的长度
def longest_increasing_subseq_dp(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # 初始每个元素自身是长度为 1 的子序列

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

nums = [4,6,8,7,5,9,2,3,10,4,5,7,8]
print(longest_increasing_subseq_dp(nums))
# LIS: [2, 3, 7, 18] 或 [2, 5, 7, 18]
# 输出: 4


import bisect
def longest_increasing_subseq_greed(nums):
    tails = []
    backtracks = []
    for num in nums:
        index = bisect.bisect_left(tails, num)  # 在 tails 中找到 >= num 的位置
        if index == len(tails):
            tails.append(num)  # 新增一个更长的序列
            if index == 0:
                backtracks.append(float('inf')) 
            else:
                backtracks.append(tails[-1]) 
        else:
            tails[index] = num  # 从index开始到最后的tails元素被顺序更新，才是更优化的子串
    return backtracks, len(tails)


backtracks, len =     longest_increasing_subseq_greed(nums)
print(backtracks)
print(len)
