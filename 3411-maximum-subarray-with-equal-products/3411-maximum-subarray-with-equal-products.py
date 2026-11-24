class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        left = 0
        ans = 2
        used = set()

        for right in range(n):
            x = nums[right]
            factors = set()

            # Find distinct prime factors of x
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.add(d)
                    while x % d == 0:
                        x //= d
                d += 1

            if x > 1:
                factors.add(x)

            # Shrink window until factors don't overlap
            while used & factors:
                y = nums[left]
                d = 2

                while d * d <= y:
                    if y % d == 0:
                        used.discard(d)
                        while y % d == 0:
                            y //= d
                    d += 1

                if y > 1:
                    used.discard(y)

                left += 1

            used.update(factors)
            ans = max(ans, right - left + 1)

        return ans