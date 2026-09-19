class Solution(object):
    def longestPalindrome(self, s):
        count = {}
        ans = 0
        odd = 0

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for n in count.values():
            ans += (n // 2) * 2
            if n % 2:
                odd = 1

        return ans + odd