import json

#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
# There are various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
#     Trie() Initializes the trie object.
#     void insert(String word) Inserts the string word into the trie.
#     boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#     boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
# https://leetcode.com/problems/implement-trie-prefix-tree/




class Trie:

    def __init__(self):
        self.__word_set = set()
        self.__prefix_set = set()

    def insert(self, word: str) -> None:
        self.__word_set.add(word)
        for i in range(len(word)) :
            self.__prefix_set.add(word[:i+1])

    def search(self, word: str) -> bool:
        return word in self.__word_set

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.__prefix_set


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)    
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out :        
        while True:
            command_line = f_in.readline().rstrip()
            arg_line = f_in.readline().rstrip()
            if not(command_line and arg_line) :
                break
            
            commands = json.loads(command_line)
            args = json.loads(arg_line)
            
            obj = None
            result = ()
            for command, arg in zip(commands, args) :
                if command == 'Trie' :
                    obj = Trie()
                    result = result + (None, )
                elif command == 'insert' :
                    result = result + (obj.insert(str(arg)), )
                elif command == 'search' :
                    result = result + (obj.search(str(arg)), )
                elif command == 'startsWith' :
                    result = result + (obj.startsWith(str(arg)), )

            f_out.write(json.dumps(result) + '\n')
