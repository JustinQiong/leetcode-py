from typing import List

"""
2788. Split Strings by Separator
Just Split each word and append in a list if it is not empty.
"""
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        li = []
        for word in words:
            for w in word.split(separator):
                if w != "":
                    li.append(w)

        return li