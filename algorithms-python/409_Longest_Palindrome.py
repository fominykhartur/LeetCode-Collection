'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = list(set(s))
        counter = {}
        for i in letters:
            counter.update([(i,s.count(i))])

        isOdd = False
        for i in counter:
            if counter[i]%2!=0:
                isOdd = True
                break

        res = sum(counter[i] for i in counter if counter[i]%2==0) + sum(counter[i]-1 for i in counter if counter[i]%2!=0)

        return res+(1 if isOdd else 0)