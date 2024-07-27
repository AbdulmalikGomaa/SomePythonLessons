class Solution:


    def __init__(self, target, *nums):

        self.nums = nums
        self.target = target


    def sol(self):

        for no in self.nums:

            if self.target - no in self.nums:

                print([self.nums.index(no), self.nums.index(self.target - no)])
                break


soo = Solution(19, 21, 4,  55, -62, 21, 1, 2, 44, -12, 47, 2, 10, 4, 9)
soo.sol()
