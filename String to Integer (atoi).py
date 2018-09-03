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





