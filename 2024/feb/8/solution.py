"""
8. String to Integer(atoi)
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        res, i, sign, length = 0, 0, 1, len(s)
        int_max, int_min, bound = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if not s:
            return 0

        while s[i] == ' ':
            i += 1
            if i == length:
                return 0

        if s[i] == '-':
            sign = -1

        if s[i] in '+-':
            i += 1

        for j in range(i, length):
            if not '0' <= s[j] <= '9':
                break;

            if res > bound or (res == bound and s[j] > '7'):
                return int_max if sign == 1 else int_min

            res = res * 10 + ord(s[j]) - ord('0')
            j += 1

        return res * sign