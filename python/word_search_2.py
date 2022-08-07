import json
from typing import DefaultDict, Tuple
from collections import defaultdict

#
# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.
#
# https://leetcode.com/problems/word-search-ii/submissions/

class Solution:
    __m_width = 0
    __m_heigth = 0
    __m_word_length = 0
    __m_dic_checked = defaultdict(int)
    
    def __dfsBoard(self, board: list[list[str]], word: str, i: int, k: int, i_word: int = 0) -> bool :
        if self.__m_dic_checked[(i, k, i_word)] > 1 :
            return False        
        self.__m_dic_checked[(i, k, i_word)] += 1
        
        if i_word >= self.__m_word_length : # word is already full checked
            return True       

        if k < 0 or k >= self.__m_heigth or i < 0 or i >= self.__m_width : # checked pos is out of board
            return False

        if word[i_word] != board[k][i] : # checked pos in not equal to checked letter
            return False

        orig, board[k][i] = board[k][i], '#' # change letter to exclude recursion

        for new_i, new_k in (i-1, k), (i+1, k), (i, k-1), (i, k+1) :
            if self.__dfsBoard(board, word, new_i, new_k, i_word+1) : # recursive call to all bounded cells
                board[k][i] = orig        
                return True

        board[k][i] = orig
        return False # wasn't found another letters of word

    def __exist(self, board: list[list[str]], word: str) -> bool:
        self.__m_heigth = len(board)
        self.__m_width = len(board[0])
        self.__m_word_length = len(word)
        self.__m_dic_checked.clear()

        for k in range(self.__m_heigth) :
            for i in range(self.__m_width) :
                if self.__dfsBoard(board, word, i, k) :
                    return True

        return False
    
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        return [ word for word in words if self.__exist(board, word)]
        


if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out :
        board_line = f_in.readline().rstrip()
        word_line = f_in.readline().rstrip()
        while board_line and word_line:
            board = json.loads(board_line)
            words = json.loads(word_line)

            exec = Solution()
            res = exec.findWords(board, words) # TODO change on real file name    

            f_out.write(json.dumps(res) + '\n')
            board_line = f_in.readline().rstrip()
            word_line = f_in.readline().rstrip()
