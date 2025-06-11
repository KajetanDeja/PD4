from typing import List


def zadanie1(nums: List[int]) -> List[int]:
    if not nums:
        return []
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_index = max(range(n), key=lambda x: dp[x])
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]
    return lis[::-1]
