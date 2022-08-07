import json
from itertools import islice

# 448. Find All Numbers Disappeared in an Array - Easy
# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution_old: # complexity: O(n) time and O(n) space
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        res = [1] * len_nums
        for num in nums:
            res[num-1] = 0

        return [i+1 for i in range(len_nums) if res[i]]

class Solution: # complexity: O(n) time and O(1) space
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            val = nums[i]
            while val:
                nums[val-1], val = 0, nums[val-1]
        
        return [i+1 for i, v in enumerate(nums) if v]
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.findDisappearedNumbers(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
