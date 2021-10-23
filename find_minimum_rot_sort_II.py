import json
from itertools import islice

# 154. Find Minimum in Rotated Sorted Array II = # Hard
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,4,4,5,6,7] might become:
#     [4,5,6,7,0,1,4] if it was rotated 4 times.
#     [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
# You must decrease the overall operation steps as much as possible.
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums)-1
        while left+1 < right:
            mid = (left+right)//2

            if nums[right] == nums[left]:
                right -= 1
            elif nums[right] < nums[mid]:
                left = mid
            else:
                right = mid

        return min(nums[left], nums[right])


if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.findMin(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
