# Given an integer array nums of length n, 
# you want to create an array ans of length 2n where ans[i] == nums[i] 
# and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# LEETCODE EASY QUESTION
def getConcatenation(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * n * 2
    for i in range(n * 2):
        ans[i] = nums[i%n]
    return ans