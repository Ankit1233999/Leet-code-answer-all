class Solution(object):
    def isArraySpecial(self, nums, queries):
       

        n = len(nums)

        prefix = [0] * n

        for i in range(1, n):

            prefix[i] = prefix[i-1]

            if nums[i] % 2 == nums[i-1] % 2:
                prefix[i] += 1


        ans = []

        for start, end in queries:

            if prefix[end] - prefix[start] == 0:
                ans.append(True)

            else:
                ans.append(False)

        return ans