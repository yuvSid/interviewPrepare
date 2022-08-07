import json

# 151. Reverse Words in a String - # Medium
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. 
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. Do not include any extra spaces.
#
# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word for word in reversed(s.split(' ')) if len(word))
            

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            if not (readen_line):
                break
            readen = json.loads(readen_line)

            exec = Solution()
            res = exec.reverseWords(readen)    

            f_out.write(json.dumps(res) + '\n')
