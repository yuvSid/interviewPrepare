import json
from itertools import islice

# 75. Sort Colors - # Medium
# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
#
# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_pos = [0, 0, 0] # pos after 0, to right from 0, to left from 1
        for num in nums:
            color_pos[num] += 1

            if color_pos[0]:
                nums[color_pos[0]-1] = 0
            if color_pos[1]:
                nums[color_pos[0]+color_pos[1]-1] = 1
            if color_pos[2]:
                nums[color_pos[0]+color_pos[1]+color_pos[2]-1] = 2

class Solution_Smarter: #dutch national flag problem https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    def sortColors(self, nums: list[int]) -> None:
        red, white, blue = 0, 0, len(nums)-1 # red point to first white after res, white point to checked element, blue points to first non blue element
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            elif nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution_Smarter()
            nums = json.loads(args_raw[0])
            exec.sortColors(nums)    

            f_out.write(json.dumps(nums) + '\n')
