""" 006 - ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a
given number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a
number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = []
        if numRows < 3:
            period = numRows
        else:
            period = 2 * numRows - 2
        for i in xrange(numRows):
            if i==0 or i==numRows-1:
                result.append(s[i::period])
            else:
                s1 = s[i::period]
                s2 = s[period-i::period]
                s3 = [None]*(len(s1)+len(s2))
                s3[::2] = s1
                s3[1::2] = s2
                result.append(''.join(s3))
        return ''.join(result)
