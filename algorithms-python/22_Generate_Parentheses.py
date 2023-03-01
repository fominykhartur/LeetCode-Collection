'''

'''


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate(count = n, res=[])


    def generate(self, count, s="", left=0, right=0, res=[]):
        if left == count and right == count:
            print(s)
            res.append(s)
        else:
            if left < count:
                self.generate(count, s+"(", left+1, right,res)
            if right < left:
                self.generate(count, s+")", left, right+1,res)
        return res

test = Solution()
print(test.generateParenthesis(1))
print(test.generateParenthesis(2))
print(test.generateParenthesis(3))