'''!!!!
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''

class Solution(object):
    def findAnagrams(self, s, p):

        n = len(s)
        m = len(p)
        
        p = Counter(p)                    # Convert list of anagram letters to a Counter (hashtable)
        ans = []
           
        window = None
        for i in range(0,n-m+1):
            if i == 0: 
                window = Counter(s[:m])   # Initialize window with beginning of s => length = length of anagram letters
            else:    
                window[s[i-1]] -= 1       # Move window to right: 1. remove character on the left
                window[s[i+m-1]] += 1     #                       2. add character on the right
            if len(window - p) == 0:      # Check if window is anagram (direct comparison of counters does not work with 0 entries)
                ans.append(i)
                
        return ans