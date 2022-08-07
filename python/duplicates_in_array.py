import json

#
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
# and each integer appears once or twice, return an array of all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/


def findDuplicates(nums: list[int]) -> list[int]:
    result = []
    nums_checked = set()

    for num in nums :
        if num in nums_checked :
            result.append(num)
        else:
            nums_checked.add(num)

    return result

    # seen = set()
    # return [x for x in nums if x in seen or seen.add(x)]
            
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out :
        readen_line = f_in.readline().rstrip()
        while readen_line :
            lst = json.loads(readen_line)

            res = findDuplicates(lst)

            f_out.write(json.dumps(res) + '\n')
            readen_line = f_in.readline().rstrip()
