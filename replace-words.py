'''
## Problem3
Replace Words (https://leetcode.com/problems/replace-words/)

TC:
O(N * L + M * W)

( Building Trie: O(N * L) — where N is number of roots and L is max length of a root.

Replacing words: O(M * W) — where M is number of words in sentence and W is average length of a word. )

SC: O(N * L) 
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    def isPrefix(self,word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                return word
            node = node.children[char]
            prefix += char
            if node.is_end:
                return prefix
        return word
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        words = sentence.split()
        replaced = [trie.isPrefix(word) for word in words]
        return " ".join(replaced)
        