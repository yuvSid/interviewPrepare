import json

#
# Given three integer arrays nums1, nums2, and nums3, 
# return a distinct array containing all the values that are present in at least two out of the three arrays. 
# You may return the values in any order. 
#
# https://leetcode.com/contest/weekly-contest-262/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        set1, set2, result_set = set(), set(), set()

        for num in nums1:
            set1.add(num)

        for num in nums2:
            if num in set1:
                result_set.add(num)
            else:
                set2.add(num)
        
        for num in nums3:
            if num in set1 or num in set2:
                result_set.add(num)
        
        return list(result_set)

    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            num1 = f_in.readline().rstrip()
            num2 = f_in.readline().rstrip()
            num3 = f_in.readline().rstrip()
            if not (num1 and num2 and num3):
                break

            num1_parsed = json.loads(num1)
            num2_parsed = json.loads(num2)
            num3_parsed = json.loads(num3)
            
            obj = Solution()
            res = obj.twoOutOfThree(num1_parsed, num2_parsed, num3_parsed) # TODO change on real file name    

            f_out.write(json.dumps(res) + '\n')
