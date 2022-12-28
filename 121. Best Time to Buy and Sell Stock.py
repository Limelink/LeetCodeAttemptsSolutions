"""LeetCode 121. Best Time to Buy and Sell Stock"""

def maxProfit(prices: list) -> int:
    """this function finds the highest difference between each number and the numbers after it in a list."""

    turnout = 0
    profits = []
    for i in range(len(prices)):
        # print(f"buying price is: {prices[i]}")
        for j in range(i, len(prices)):
            turnout = (prices[i] - prices[j])
            # print(f"If sold on the {j}. day for {prices[j]} the profit is: {-turnout}")
            profits.append(-turnout)

    return max(profits)

def maxProfit2(prices: list) -> int:
    """Another try at a solution"""

    turnout = 0
    currentMax = 0
    maxIndex = 0
    for i in range(len(prices)):
        if i >= maxIndex:
            currentMax = max(prices[i:])
            maxIndex = prices.index(currentMax)

        if (currentMax - prices[i]) > turnout:
            turnout = currentMax - prices[i]

    return turnout


maxProfit([7,1,5,3,6,4])

print(maxProfit2([7,1,5,3,6,4]))
print(maxProfit2([7,6,4,3,1]))