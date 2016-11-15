""" 029 - Divide Two Integers
https://leetcode.com/problems/divide-two-integers/

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        count = 0
        if divisor == 0:
            return -1
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            div = divisor
            shift = 0
            while div << 1 <= dividend:
                div = div << 1
                shift += 1
            dividend = dividend - div
            count += 1 << shift
        if sign * count > 2147483647:
            return 2147483647
        elif sign * count < -2147483648:
            return -2147483648
        else:
            return sign * count
