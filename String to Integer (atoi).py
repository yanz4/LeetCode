'''Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.'''










class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        num = str.split()
        if len(num) == 0:
            return 0
        else:
            num = str.split()[0]

        from functools import reduce
        sign = False
        a = num.split('.')
        l = a[0]
        summ = 0
        summr = 0
        print(a, l)
        if len(l) == 0:
            return 0
        elif len(l) == 1:
            if ord(l[0]) <= ord('9') and ord(l[0]) >= ord('0'):
                return int(l[0])
            else:
                return 0
        else:
            if l[0] in ['-', '+']:
                if l[0] == '-':
                    sign = True
                l = l[1:]
            for i in l:
                if ord(i) <= ord('9') and ord(i) >= ord('0'):
                    summ = 10 * summ + int(i)
                else:
                    break

        if len(a) > 1:
            r = a[1]
            for i in range(len(r)):
                i += 1
                if ord(i) <= ord('9') and ord(i) >= ord('0'):
                    summr = 10 ** (-i) * int(r[i]) + summr
                else:
                    break
        if sign:
            c = -(summ + summr)
            if c < INT_MIN:
                return INT_MIN
            else:
                return c
        else:
            d = summ + summr
            if d > INT_MAX:
                return INT_MAX
            else:
                return d





