class Solution(object):
    def concatWithReverse(self, nums):
        ans = []

        # Add original array
        for num in nums:
            ans.append(num)

        # Add reversed array
        for i in range(len(nums) - 1, -1, -1):
            ans.append(nums[i])

        return ans
        