import json

#
# Given a string s, find the length of the longest substring without repeating characters.
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#

def lengthOfLongestSubstring(s: str) -> int:
    max_str = 0
    cur_start = 0
    seen_letter = {}

    for i, letter in enumerate(s) : 
        if letter in seen_letter and seen_letter[letter] >= cur_start:
            max_str = max(max_str, i-cur_start)
            cur_start = seen_letter[letter] + 1

        seen_letter[letter] = i
    
    return max(max_str, len(s) - cur_start)   


if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out :
        readen_line = f_in.readline()
        while readen_line :
            lst = json.loads(readen_line)

            res = lengthOfLongestSubstring(lst)     

            f_out.write(json.dumps(res) + '\n')
            readen_line = f_in.readline()
