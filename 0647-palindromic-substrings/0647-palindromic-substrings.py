
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left, right):
            total = 0

            while left >= 0 and right < n and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1

            return total

        for i in range(n):
           
            count += expand(i, i)

            
            count += expand(i, i + 1)

        return count
