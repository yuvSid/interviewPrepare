import json
import math

# 279. Perfect Squares - Medium
# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; 
# in other words, it is the product of some integer with itself. 
# For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
#
# https://leetcode.com/problems/perfect-squares/

class Solution:
    __min_nums = [0]

    def numSquares(self, n: int) -> int:
        for i in range(len(self.__min_nums), n+1):
            if math.isqrt(i) ** 2 == i:
                self.__min_nums.append(1)
                continue
            for k in range(1, math.isqrt(i) + 1):
                if i < len(self.__min_nums): 
                    self.__min_nums[i] = min(self.__min_nums[i], 1+self.__min_nums[i-k**2]) 
                else:
                    self.__min_nums.append(1 + self.__min_nums[i-k**2])

        return self.__min_nums[n]

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            if not readen_line:
                break
            readen = int(readen_line)

            exec = Solution()
            res = exec.numSquares(readen)    

            f_out.write(json.dumps(res) + '\n')
