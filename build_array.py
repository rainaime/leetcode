# RETURNS AN ARRAY WWHERE
# ans[i] = nums[nums[i]
# LEETCODE EASY QUESTION
def buildArray(self, nums: List[int]) -> List[int]:
    ans = [0] * len(nums)
    for i in range(len(nums)):
        ans[i] = nums[nums[i]]
    return ans