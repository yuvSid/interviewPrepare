import json
from itertools import islice

# 540. Single Element in a Sorted Array - Medium
# You are given a sorted array consisting of only integers where every 
# element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:            
            mid = (left + right) // 2
            
            if ( mid % 2 ): # check nums near with logic check if checking position is odd or not 
                if (nums[mid] == nums[mid+1]):
                    right = mid - 1
                else:
                    left = mid + 1 
            else:
                if (nums[mid] == nums[mid+1]):
                    left = mid+2
                else:
                    right = mid               
        
        return nums[left]
        
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.singleNonDuplicate(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
