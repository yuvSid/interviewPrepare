import json

# 283. Move Zeroes - # Easy
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements. Note that you must do this 
# in-place without making a copy of the array.
#
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for check in range(len(nums)):
            if nums[check] != 0:
                nums[check], nums[zero] = nums[zero], nums[check]
                zero += 1
        
        
        	  
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            if not (readen_line):
                break
            readen = json.loads(readen_line)

            exec = Solution()
            exec.moveZeroes(readen)    

            f_out.write(json.dumps(readen) + '\n')
