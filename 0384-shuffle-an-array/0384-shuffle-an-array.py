import random

class Solution:

    def __init__(self, nums):
        self.original = nums[:]
        self.array = nums[:]

    def reset(self):
        self.array = self.original[:]
        return self.array

    def shuffle(self):
        n = len(self.array)

        for i in range(n):
            j = random.randint(i, n - 1)

           
            self.array[i], self.array[j] = self.array[j], self.array[i]

        return self.array