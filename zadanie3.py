from typing import List


def zadanie3(n: int) -> List[List[int]]:
    result = []

    def backtrack(remaining: int, path: List[int], start: int):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, remaining + 1):
            path.append(i)
            backtrack(remaining - i, path, i)
            path.pop()

    backtrack(n, [], 1)
    return result
