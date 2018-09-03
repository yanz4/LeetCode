class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = 0

        a = ''
        start = 0

        counter = 0
        for i, j in enumerate(s):

            if j in a:

                start += (1 + a.find(j))
                a += j
                a = s[start:i + 1]

            else:
                a += j

            maximum = max(i - start + 1, maximum)

        return maximum
