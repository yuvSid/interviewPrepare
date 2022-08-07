import json

# 309. Best Time to Buy and Sell Stock with Cooldown - Medium
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution: # Naive approach calculating and saving all previous combinations
    def maxProfit(self, prices: list[int]) -> int:
        max_to_day = []
        for day in range(len(prices)):
            max_to_day.append(max_to_day[day-1] if day-1 > 0 else 0) 
            for buy in range(day): # check all combinations
                max_to_day[day] = max(max_to_day[day], prices[day] - prices[buy] + (max_to_day[buy-2] if buy-2 > 0 else 0)) #calculate profit from selling and add max profit to day before cooldown

        return max_to_day[len(prices)-1]

class Solution2: # Faster solution, using state DP with state machine
    def maxProfit(self, prices: list[int]) -> int:
    #           rest|      hold|sold|
        profit = [[0, -prices[0], 0]]
        for i in range(len(prices)-1):
            profit.append([ # describe of how to approach states, if more than one way - find where max profite will be
                max(profit[i][0], profit[i][2]), # rest -> from prev rest or prev sold states
                max(profit[i][1], profit[i][0] - prices[i+1]), # hold state -> from prev hold state or from prev rest state by buying stocks by cur price(subtract cur price for profit correct storing)
                profit[i][1] + prices[i+1] # sold state -> from prev hold state by adding current stocks price
            ])  
        
        return max(profit[-1][0], profit[-1][2])

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            if not (readen_line):
                break
            readen = json.loads(readen_line)

            exec = Solution2()
            res = exec.maxProfit(readen)    

            f_out.write(json.dumps(res) + '\n')
