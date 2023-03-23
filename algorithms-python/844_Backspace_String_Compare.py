'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while "#" in s:
            p = re.search(f"\w?#", s)[0] 
            s = s.replace(p,"",1)

        while "#" in t:
            p = re.search(f"\w?#", t)[0] 
            t = t.replace(p,"",1)

        return True if s==t else False