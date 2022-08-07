import json

# 496. Next Greater Element I - # Easy
#
# The next greater element of some element x in an array is the first greater element 
# that is to the right of x in the same array. You are given two distinct 0-indexed 
# integer arrays nums1 and nums2, where nums1 is a subset of nums2. # For each 0 <= i
# < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next 
# greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        search = {val: i for i, val in enumerate(nums1)}
        found = dict()
        nums1 = [-1] * len(nums1)
        for num in nums2:
            del_key = []
            for key, value in found.items():
                if num > key:
                    nums1[value] = num
                    del_key.append(key)
            for key in del_key:
                del found[key]
                
            if num in search:
                found[num] = search[num]
                del search[num]

        return nums1    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            from_line = f_in.readline().rstrip()
            in_line = f_in.readline().rstrip()
            if not (from_line and in_line):
                break
            readen = json.loads(from_line)
            in_list = json.loads(in_line)

            exec = Solution()
            res = exec.nextGreaterElement(readen, in_list)    

            f_out.write(json.dumps(res) + '\n')
