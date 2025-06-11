from typing import List


def zadanie2(nums: List[int]) -> List[int]:
    max_sum = current_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum or (
            current_sum == max_sum and i - temp_start > end - start
        ):
            max_sum = current_sum
            start = temp_start
            end = i

    return nums[start : end + 1]
