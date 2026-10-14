
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        current = []

        def backtrack(start):
            if len(current) == k:
                result.append(current.copy())
                return

            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1)
                current.pop()

        backtrack(1)
        return result
