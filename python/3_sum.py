import json
from itertools import islice
from itertools import combinations

# 15. 3Sum - # Medium
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
#
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        sums = dict()

        nums.sort()
        for i in range(2, len(nums)):   
            for l in range(i-1):
                if (sum_val := nums[l]+nums[i-1]) not in sums:
                    sums[sum_val] = set()
                sums[sum_val].add((nums[l], nums[i-1]))

            if 0-nums[i] in sums:
                for sets in sums[0-nums[i]]:
                    res.add((sets[0], sets[1], nums[i]))

        return [sets for sets in res]    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.threeSum(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
