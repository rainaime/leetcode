# FOR EACH KID IN LIST CANDIES WITH NUMBER OF CANDIES, CHECK IF IT'S POSSIBLE TO ADD
# AN EXTRA CANDY AND HAVE THEM HAVE THE MOST CANDIES
# LEETCODE EASY QUESTION
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    outputCandy = []
    maxCandy = max(candies)
    for kid in candies:
        if kid + extraCandies < maxCandy:
            outputCandy.append(False)
        else:
            outputCandy.append(True)
    return outputCandy
        