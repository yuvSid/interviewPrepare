import json

# 977. Squares of a Sorted Array - Easy
#
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
#
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res, len_nums = [], len(nums)
        for pos_i in range(len_nums):
            if nums[pos_i] >= 0:
                break
        
        neg_i = pos_i-1 
        while pos_i < len_nums or neg_i >= 0:
            if neg_i < 0 or (pos_i < len_nums and nums[pos_i] <= -nums[neg_i]):
                res.append(nums[pos_i]**2)
                pos_i += 1
            else:
                res.append(nums[neg_i]**2)
                neg_i -= 1

        return res

            
                    


if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            readen_nums = f_in.readline().rstrip()
            if not readen_nums:
                break
            nums = json.loads(readen_nums)

            exec = Solution()
            res = exec.sortedSquares(nums)    

            f_out.write(json.dumps(res) + '\n')
