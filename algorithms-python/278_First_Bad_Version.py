'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
'''


def isBadVersion(n):
    if n >= 1702766719:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n <= 5:
            for i in range(1,n+1):
            	if isBadVersion(i)==True:
            		return i
        b = 1
        prevMid = 1
        while True:
            mid = (b + n) // 2
            print(mid)
            if isBadVersion(mid) == True:
                print(mid, prevMid)
                if mid - prevMid > 100:
                	n = mid
                	b = prevMid
                	continue
                for i in range(mid, prevMid - 1, -1):
                    if isBadVersion(i) == True:
                        continue
                    else:
                        return i + 1
            else:
                prevMid = mid
                b = mid + 1
                continue


test = Solution()
print(test.firstBadVersion(2126753390))
