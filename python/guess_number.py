import json

#
# 374. Guess Number Higher or Lower
# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns 3 possible results:
#     -1: The number I picked is lower than your guess (i.e. pick < num).
#     1: The number I picked is higher than your guess (i.e. pick > num).
#     0: The number I picked is equal to your guess (i.e. pick == num).
# Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
#
# https://leetcode.com/problems/guess-number-higher-or-lower/submissions/

if __name__ == '__main__':    
    
    pick = 0
    def guess(num: int) -> int:
        return 0 if num == pick else -1 if pick < num else 1

    
    class Solution:
        def guessNumber(self, n: int) -> int: 
            return self.__guessNum(1, n)

        def __guessNum(self, left: int, right: int) -> int:
            if left >= right:
                return left
            
            new_border = (left + right) // 2
            if not (res := guess(new_border)):
                return new_border
            elif res == -1:
                return self.__guessNum(left, new_border-1)
            else:
                return self.__guessNum(new_border+1, right)
    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            readen_n = f_in.readline().rstrip()
            readen_pick = f_in.readline().rstrip()
            if not (readen_n and readen_pick):
                break
            n = int(readen_n)
            pick = int(readen_pick)

            exec = Solution()        
            res = exec.guessNumber(n) # TODO change on real file name    

            f_out.write(json.dumps(res) + '\n')
