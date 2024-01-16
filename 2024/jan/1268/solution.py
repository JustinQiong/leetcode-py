from typing import List

class Trie:
    def __init__(self):
        self.child = dict()
        self.words = list()

"""
1268. Search Suggestions System
Trie Solution:
Each Node of the trie will have a child dict and words list.
Child dict will include the chars of the next char.
Words will include the top 3 words with the prefix of the parent nodes.
"""
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def addWord(root, word):
            curr = root
            for ch in word:
                if ch not in curr.child:
                    curr.child[ch] = Trie()
                curr = curr.child[ch]
                curr.words.append(word)
                curr.words.sort()
                if len(curr.words) > 3:
                    curr.words.pop()

        root = Trie()
        for product in products:
            addWord(root, product)

        curr = root
        failed = False
        res = list()
        for ch in searchWord:
            if failed or ch not in curr.child:
                res.append(list())
                failed = True
            else:
                curr = curr.child[ch]
                res.append(curr.words)

        return res
