""" 005 - Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may
assume that the maximum length of s is 1000
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = s[0:1]
        max_len = 1
        len_s = len(s)
        for i in xrange(len_s):
            while True:
                new_len = max_len+1
                min_range = i - (new_len>>1)
                max_range = i + (new_len>>1) + (new_len&1)
                if min_range < 0 or max_range > len_s:
                    break
                str = s[min_range:max_range]
                if str == str[::-1]:
                    longest = str
                    max_len = len(str)
                else:
                    break
            while True:
                new_len = max_len+2
                min_range = i - (new_len>>1)
                max_range = i + (new_len>>1) + (new_len&1)
                if min_range < 0 or max_range > len_s:
                    break
                str = s[min_range:max_range]
                if str == str[::-1]:
                    longest = str
                    max_len = len(str)
                else:
                    break

        return longest

if __name__ == "__main__":
    solution = Solution()
    test = ["1zababa5231", "xcfabbaf", "zxabr"]
    for s in test:
        print "{} = {}".format(s, solution.longestPalindrome(s))
