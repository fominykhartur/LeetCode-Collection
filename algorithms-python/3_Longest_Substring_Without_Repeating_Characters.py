'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = []
        tempStr = ''
        while i < len(s):
            if s[i] not in tempStr:
                tempStr+= s[i]
            else:
                res.append(len(tempStr))
                tempStr = tempStr[tempStr.index(s[i])+1:] + s[i]

            i+=1
        res.append(len(tempStr))
        return max(res)


test = Solution()
print(test.lengthOfLongestSubstring("ohvhjdml"))