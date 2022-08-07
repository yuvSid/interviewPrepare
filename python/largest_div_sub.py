import json
from itertools import islice

# 368. Largest Divisible Subset - Medium
# Given a set of distinct positive integers nums, return the largest subset 
# answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
#     answer[i] % answer[j] == 0, or
#     answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.
#
# https://leetcode.com/problems/largest-divisible-subset/

class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        nums_len = len(nums)
        info = [(0, 0)] * nums_len
        
        # go through sorted list check that larger num can be moduled by lower, if yes increase subset result in turple inside info list
        for j in range(nums_len-1, 0, -1):
            for i in range(j):
                if (nums[j] % nums[i] == 0 and (sub_len := info[j][0] + 1) > info[i][0]):
                    info[i] = (sub_len, j)
        
        # backtrack realisation
        index = info.index(max(info, key=lambda inf : inf[0]))
        res = [nums[index]]
        while info[index][0]:
            index = info[index][1]
            res.append(nums[index])

        return res

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.largestDivisibleSubset(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
