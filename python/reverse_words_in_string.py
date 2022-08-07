import json

# 557. Reverse Words in a String III - # Easy
# Given a string s, reverse the order of characters in each word within
# a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))

class Solution2:
    def reverseWords(self, s: str) -> str:
        res_s = ''
                
        word_start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                res_s = res_s + s[i-1:word_start:-1] + s[word_start] + ' '
                word_start = i+1

        res_s = res_s + s[i:word_start:-1] + s[word_start]
        return res_s 
    

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
