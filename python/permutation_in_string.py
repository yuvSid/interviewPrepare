import json

# 567. Permutation in String - # Medium
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise. In other words, return true if one of 
# s1's permutations is the substring of s2.
#
# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map_fast = [0] * 26
        def isCorrectWindow() -> bool: # check that all letters was duplicated in window
            for i in map_fast:
                if i:
                    return False
            return True

        if ((len_s1 := len(s1)) > (len_s2 := len(s2))): 
            return False

        ascii_a = ord('a')
        for i in range(len_s1): # create window of s1 size and count all numbers, s1 plus, s2 minus
            map_fast[ord(s1[i]) - ascii_a] += 1
            map_fast[ord(s2[i]) - ascii_a] -= 1

        if isCorrectWindow():
            return True

        for i in range(len_s2 - len_s1): # move window to left and count left letter back and right letter (new) to minus
            map_fast[ord(s2[i]) - ascii_a] += 1
            map_fast[ord(s2[len_s1 + i]) - ascii_a] -= 1

            if isCorrectWindow():
                return True

        return False
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            from_line = f_in.readline().rstrip()
            in_line = f_in.readline().rstrip()
            if not (from_line and in_line):
                break
            from_str = json.loads(from_line)
            in_str = json.loads(in_line)

            exec = Solution()
            res = exec.checkInclusion(from_str, in_str)    

            f_out.write(json.dumps(res) + '\n')
