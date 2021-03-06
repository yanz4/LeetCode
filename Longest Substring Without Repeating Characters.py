'''Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.'''






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
