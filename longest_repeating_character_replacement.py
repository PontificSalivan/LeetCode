class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        left_border = 0
        char_frequency = {}
        max_substring = 0
        # Перемещаем правую границу
        for right_border in range(len(s)):
            # Добавляем букву в dict и добавляем букве +1 к ее частоте
            char_frequency[s[right_border]] = char_frequency.get(s[right_border], 0) + 1
            # Размер текущего промежутка
            cells_count = right_border - left_border + 1
            # Не меняем левую границу, пока k позволяет нам заменять буквы,
            # максимальная частота которых меньше частоты самой повторяющейся буквы на текущем промежутке
            if cells_count - max(char_frequency.values()) <= k:
                max_substring = max(max_substring, cells_count)
            else:
                # Убираем крайнюю слева букву, вычитаем 1 из dict
                char_frequency[s[left_border]] -= 1
                # Новая левая граница
                left_border += 1

        return max_substring


# test
slt = Solution()
print(slt.characterReplacement("ABAB", 2))
print(slt.characterReplacement("AAAA", 0))
print(slt.characterReplacement("AABABBA", 1))
print(slt.characterReplacement("AAAB", 0))
print(slt.characterReplacement("A", 1))
print(slt.characterReplacement("A", 0))
assert slt.characterReplacement("ABAB", 2) == 4
assert slt.characterReplacement("AABABBA", 1) == 4
assert slt.characterReplacement("AABBBBA", 1) == 5
assert slt.characterReplacement("BABBBBA", 2) == 7
assert slt.characterReplacement("AAAA", 0) == 4
assert slt.characterReplacement("AAAB", 0) == 3
assert slt.characterReplacement("A", 1) == 1
assert slt.characterReplacement("A", 0) == 1

