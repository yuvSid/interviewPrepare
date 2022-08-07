import json

# 35. Search Insert Position - Easy
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
#
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left if target <= nums[left] else left + 1
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            readen_nums = f_in.readline().rstrip()
            readen_target = f_in.readline().rstrip()
            if not (readen_nums and readen_target):
                break
            readen = json.loads(readen_nums)
            target = int(readen_target)

            exec = Solution()
            res = exec.searchInsert(readen, target)    

            f_out.write(json.dumps(res) + '\n')
