import json
from itertools import islice

# 53. Maximum Subarray - Easy
# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
#
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        class Result:
            def __init__(self, val=0):
                self.to_left = val
                self.to_right = val
                self.sum = val
                self.max_sum = val

        def devAndConq(nums, left, right) -> Result:         
            if left == right:
                return Result(nums[left])         

            res_l = devAndConq(nums, left, (left+right)//2)
            res_r = devAndConq(nums, (left+right)//2+1, right)
            
            res = Result()
            res.to_left = max(res_l.to_left, res_l.sum+res_r.to_left)
            res.to_right = max(res_l.to_right + res_r.sum, res_r.to_right)
            res.sum = res_l.sum + res_r.sum
            res.max_sum = max(res_l.max_sum, res_r.max_sum, res_l.to_right + res_r.to_left)
            return res
            
        res_end = devAndConq(nums, 0, len(nums)-1)
        return max(res_end.to_left, res_end.to_right, res_end.sum, res_end.max_sum)


        
    def maxSubArrayStraight(self, nums: list[int]) -> int:
        # straight silution O(n)
        largest = nums[0]
        prev = 0
        for num in nums:
            largest = max(largest, num+prev)
            prev = max(num+prev, 0)
        
        return largest



    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.maxSubArray(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
