class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize variables hold, sell, and rest to the inverse of the first element in the input list, 0, and 0 respectively.
        hold = -prices[0]
        sell = 0
        rest = 0

        # Iterate through each price in the input list. On each iteration, store the previous hold value in a temp variable, and update the hold, rest, and sold variables.
        for price in prices:
            prev_hold = hold
           
            # Hold is the max between the previous hold value and the value of buying (previous rest value minus stock price)
            hold = max(hold, rest - price)
            # Rest is the max between the previous rest value and the previous sell value
            rest = max(rest, sell)
            # Sell is the profit from selling the stock that was held from the previous day (represented by prev_hold + price)
            sell = prev_hold + price

        # Return the maximum between the sell and rest
        return max(sell, rest)