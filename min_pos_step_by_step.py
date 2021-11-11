import json
from itertools import islice

# 1413. Minimum Value to Get Positive Step by Step Sum - Easy
# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.
#
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        startVal = 1
        val = 1
        for num in nums:
            if (val := val + num) < 1:
                startVal += 1 - val
                val = 1
        
        return startVal
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.minStartValue(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
