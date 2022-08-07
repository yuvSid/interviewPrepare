import json
from itertools import islice

# 461. Hamming Distance - Easy
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.
#
# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y # total XOR
        res = 0
        while x: # go through all bits and count 1
            if x & 1:
                res += 1    
            x = x >> 1

        return res
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 2
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.hammingDistance(int(args_raw[0]), int(args_raw[1]))    

            f_out.write(json.dumps(res) + '\n')
