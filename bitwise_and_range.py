import json

#
# Given two integers left and right that represent the range [left, right], 
# return the bitwise AND of all numbers in this range, inclusive.
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1          

        return left << count
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            left_line = f_in.readline().rstrip()
            rigth_line = f_in.readline().rstrip()

            if not (left_line and rigth_line):
                break
            left = json.loads(left_line)
            right = json.loads(rigth_line)

            res = Solution.rangeBitwiseAnd(Solution(), left, right)     

            f_out.write(json.dumps(res) + '\n')
