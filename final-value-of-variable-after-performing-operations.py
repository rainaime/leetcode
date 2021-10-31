# Given an array of strings operations containing a list of operations,
# return the final value of X after performing all the operations.
# LEETCODE EASY QUESTION
def finalValueAfterOperations(self, operations: List[str]) -> int:
    x = 0
    for op in operations:
        print(op)
        if '--' in op:
            x = x - 1
        else:
            x = x + 1
    return x