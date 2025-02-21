#给定一个整数数组 nums，找到其中 最长递增子序列 的长度
def longest_increasing_subseq_dp(nums):
    if not nums:
        return 0

    n = len(nums)
    #设 dp[i] 为 以 nums[i] 结尾的最长递增子序列的长度
    dp = [1] * n  # 初始每个元素自身是长度为 1 的子序列

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

nums = [6,11,1,9,2,3,10,4,5,7,8]
print(longest_increasing_subseq_dp(nums))
# LIS: [2, 3, 7, 18] 或 [2, 5, 7, 18]
# 输出: 4


import bisect
def longest_increasing_subseq_greed(nums):
    tails = []
    backtracks = {}
    for num in nums:
        index = bisect.bisect_left(tails, num)  # 在 tails 中找到 >= num 的位置
        backtracks[num] = tails[index-1] if index > 0 else float('inf')
        if index == len(tails):
            tails.append(num)  # 新增一个更长的序列
        else:
            #tails[0...index]是候选子序列，只有tails[index+1, ..., -1]的元素被顺序更新，才能取代原来的子序列
            tails[index] = num

    return backtracks, tails


backtracks, tails =     longest_increasing_subseq_greed(nums)
print(len(tails))
print(backtracks)
subseq = [tails[-1]]
prev = backtracks[subseq[0]]
while prev != float('inf'):
    subseq.insert(0, prev)
    prev = backtracks[subseq[0]]
print(subseq)

