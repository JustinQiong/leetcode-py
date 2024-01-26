"""
5. Longest Palindromic Substring
Iterate through each of the char of string s.
Expand the substring from both left and right direction.
Find out the maxLen and the correspondent left point
and return the substring.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        minLeft = 0

        i = 0
        while i < n - (maxLen / 2):
            left = i - 1
            right = i + 1
            le = 1
            while left >= 0 and s[left] == s[i]:
                left -= 1
                le += 1

            while right < n and s[right] == s[i]:
                right += 1
                le += 1

            while left >= 0 and right < n and s[right] == s[left]:
                left -= 1
                right += 1
                le += 2

            if le > maxLen:
                maxLen = le
                minLeft = left

            i += 1

        return s[minLeft + 1: minLeft + 1 + maxLen]
