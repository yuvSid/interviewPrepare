from bisect import bisect_left

#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# https://leetcode.com/problems/two-sum/

# INPUT:
# [2,7,11,15]
# 9


def twoSum(nums: list[int], target: int) -> list[int]:
    indexMap = {} # value : index
    for cur_index, value in enumerate(nums) :
        diff = target - value

        if diff in indexMap :
            return [indexMap[diff], cur_index]
        else :
            indexMap[value] = cur_index
    
    return []


if __name__ == '__main__':
    #fptr = open('OUTPUT/OUT', 'w')
    frptr = open('OUTPUT/IN', 'r')
    fptr = open('OUTPUT/OUT', 'w')
    
    lineNums = frptr.readline()
    lineTarget = frptr.readline()
    while lineNums and lineTarget :
        nums = list(map(int, lineNums.rstrip()[1 : -1].split(sep = ',')))
        target = int(lineTarget.rstrip())

        result = twoSum(nums, target)
        fptr.write(str(result) + '\n')

        lineNums = frptr.readline()
        lineTarget = frptr.readline()
    
    frptr.close()
    fptr.close()
