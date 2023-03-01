'''
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s)
        ixd, jxd = 0, 0
        reverse = False
        res = []

        while True:
            if s[i:j] == s[i:j][::-1]:
                res.append(s[i:j])
            print(s[i:j], s[i:j][::-1])
            print(i, j, ixd, jxd)

            if reverse:
                i += 1
            else:
                j -= 1

            if j == i + 1:
                j = len(s) - i
                i = ixd
                reverse = True
            if i == j - 1:
                ixd += 1
                j = len(s) - i
                reverse = False

            # j-=1
            # if j == i+1:
            #     j = len(s)-jxd
            #     i+=1
            #     jxd+=1

            # j-=1
            # if j == jxd:
            #   j = len(s)
            #   jxd += 1
            #   i+= jxd
            # else:
            #   j-=1
            # if ixd <= jxd:
            #   i+=1
            #   print("1")
            #   continue
            # if jxd <= ixd:
            #   j-=1
            #   print("2")
            #   continue
            # if i == len(s)-1:
            #   ixd+=1
            #   i = ixd
            #   print("3")
            #   # continue
            # if j == 0:
            #   jxd += 1
            #   j = len(s)-jxd
            #   print("4")
            #   # continue

        return s[i:j]


test = Solution()
print(test.longestPalindrome('qweaaaabbbbaaaaqwe'))
# print(test.longestPalindrome('aacabdkacaa'))
# print(test.longestPalindrome('lphntrsqudccteewsdmpjmgmfnxegawjclzobpnxdrvxeygafiwyqsvsecictqkmiqvrdjajfngvlhdezdpqpzjjzbhoyggrbkuzeocrpzqishvfairdvvabopyubfisxbrgnlughbrzunitwowvnsqhdtnkotitgxwzjhbgltksorygpdberdgzgvogrvwluhixfbrfhliedjylxuspjpitwlhdkneonreqrueqphirmgxtqumllqropaefddplspkrtkbmuvwkyryworojlvwzdlacuoqzokrmcgmwkopsbqjjkaoqjqbrderwzmhbhfgwvrjakyfeqcbtvlcgbsxkngymxyievihiskdmmppmmdksihiveiyxmygnkxsbgclvtbcqefykajrvwgfhbhmzwredrbqjqoakjjqbspokwmgcmrkozqoucaldzwvljorowyrykwvumbktrkpslpddfeaporqllmuqtxgmrihpqeurqernoenkdhlwtipjpsuxlyjdeilhfrbfxihulwvrgovgzgdrebdpgyrosktlgbhjzwxgtitokntdhqsnvwowtinuzrbhgulngrbxsifbuypobavvdriafvhsiqzprcoezukbrggyohbzjjzpqpdzedhlvgnfjajdrvqimkqtcicesvsqywifagyexvrdxnpbozlcjwagexnfmgmjpmdsweetccduqsrtnhpl'))
