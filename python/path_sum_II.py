import json

# 167. Two Sum II - Input array is sorted - # Easy
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] 
# where 1 <= first < second <= numbers.length. Return the indices of the two numbers, 
# index1 and index2, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. 
# You may not use the same element twice.
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # num_in = {num: [pos] if num not in num_in else num_in[num].append(pos) for pos, num in enumerate(numbers)}
        num_in = dict()
        for pos, num in enumerate(numbers):
            if num not in num_in:
                num_in[num] = [pos]
            else:
                num_in[num].append(pos)

        for i in range(len(numbers)):
            if target-numbers[i] in num_in:
                for k in num_in[target-numbers[i]]:
                    if i != k:
                        return [i+1, k+1]
        
        return [None, None]  
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            numbers_line = f_in.readline().rstrip()
            target_line = f_in.readline().rstrip()
            if not (numbers_line and target_line):
                break
            numbers = json.loads(numbers_line)

            exec = Solution()
            res = exec.twoSum(numbers, int(target_line))    

            f_out.write(json.dumps(res) + '\n')
