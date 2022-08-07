import json
from itertools import islice

# 122. Best Time to Buy and Sell Stock II - Medium
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the 
# stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        prof = 0     
        buyVal = prices[0]
        # go though list if next val is lower, save profit and buy by lower price
        for (cur, next) in zip(prices, prices[1:]):
            if cur <= next:
                continue
            if buyVal < cur:
                prof += cur - buyVal
            buyVal = next
        
        #check last:
        if buyVal < prices[-1]:
            prof += prices[-1] - buyVal

        return prof

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.maxProfit(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
