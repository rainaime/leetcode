# KEEP A RUNNING SUM OF THE NUMBERS IN LIST NUMS
# LEETCODE EASY QUESTION
def runningSum(self, nums: List[int]) -> List[int]:
    returnSum = []
    for i in range(len(nums)):
        returnSum.append(sum(nums[:i+1]))
    return returnSum