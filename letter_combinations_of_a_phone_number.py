from typing import List
from itertools import product


class Solution:
    numbers = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
               "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
               "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        combination = self.numbers[digits[0]]
        for i in digits[1:]:
            words = self.numbers[i]
            combination = ["".join(word) for word in product(combination, words)]

        return combination


# test
slt = Solution()
print(slt.letterCombinations("23"))
print(slt.letterCombinations(""))
print(slt.letterCombinations("2"))
print(slt.letterCombinations("234"))
assert slt.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert slt.letterCombinations("") == []
assert slt.letterCombinations("2") == ["a", "b", "c"]

