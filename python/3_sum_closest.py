import json
from itertools import islice

# 16. 3Sum Closest - Medium
# Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[0:3]) # check smallest numbers
        if closest >= target :
            return closest
        closest = sum(nums[-3:]) # check biggest numbers
        if closest <= target :
            return closest
        
        for i in range(len(nums)-2): # tow pointers approach
            j, k = i+1, len(nums)-1
            while j<k :
                sums = nums[i] + nums[j] + nums[k]
                if abs(target - sums) < abs(closest - target) :
                    closest = sums
                if sums == target:
                    return sums
                elif sums < target :
                    j += 1
                else :
                    k -= 1
            
        return closest
        

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 2
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.threeSumClosest(json.loads(args_raw[0]), json.loads(args_raw[1]))    

            f_out.write(json.dumps(res) + '\n')
