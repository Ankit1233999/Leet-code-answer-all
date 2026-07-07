class Solution(object):
    def reverseString(self, s):
       

        def solve(left, right):

            if left >= right:
                return

            s[left], s[right] = s[right], s[left]

            solve(left + 1, right - 1)
            

        solve(0, len(s)-1)
        