import json
from itertools import islice

# 451. Sort Characters By Frequency - # Medium
# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.
#
# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for letter in s:
            if letter not in freq:
                freq[letter]=0
            freq[letter] += 1
        return ''.join(letter[0]*letter[1] for letter in sorted(freq.items(), key = lambda x: x[1], reverse = True))

    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.frequencySort(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
