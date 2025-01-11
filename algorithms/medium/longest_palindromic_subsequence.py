#
# DP : Recursion + memoization
#
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def LPS(i, j):
            #print(f'\t(i, j) = ({i}, {j})')
            if (i, j) in memo:
                return memo[(i,j)]
            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                ans = 2 + LPS(i+1, j-1)
            else:
                ans = max(LPS(i+1, j), LPS(i, j-1))
            memo[(i,j)] = ans
            return memo[(i,j)]
        memo = dict()
        res = LPS(0, len(s)-1)
        print(f'memo = {memo}')
        return res

# Main section
for s in [
            'bbbab',
            'cbbd',
            'vgpfhgdxfl',
            #'upvgarvtptjnjkbtusgskremmcmnkfnajkuloydxevabqsgvtqoovgbolsoiddqwjuuqgejfcvykorsybarsbcacnpoicsrqkwqr',
            #'onibfnbkjdgpzfhxmwmamrosuulkovspjharpntwkjuvjzbjwrnykwvdfurnxkuuemmyxavkeowloobdgmpbxczuufgtmkcoqeqcyentbofyamtbzoklwmwxeeoicghvflguogmzbnevemnqacpsjeneepozkuqmgpqinhjyclifmxuuvnmhieyhlqcmfvifeyzjbmmnenfexedoeznaghvshlcwhigqcuxsgodwtbmhfbyrfydsbivfdzgjxveynrntlnwjdswxneksffkzdxrtmlltkrxxbsxskwjzouxqdyauklvsbbxawmdrbmytigvpfvoituonpwzlspyuliyaaepxklpeqledgfjlxbkhjdxuuekxxbpqkpznpziatwtmmrkltycyxfbbofothmyofkycaswcrphrrrndxrnkzmeumsdtpxunjrkyxnjutrbzmvxvajgnpwimvabjaxmvuamjkfapxsgdfihozwojazlnhgyj',
            #'ayddhbqpytgiarzbaxwsgwqmjtyybmvcfdwnrmgqwqwvntgnvuxhfbowwrftqyjedudlmfeiunoqhoushzmfornepqykteusfkajlczippkqvlsspytiiwktvzwubkubrvdkvwzinkcnlkhmqhuhdkttdmmwhfebqhwsqnfauhbtktjalstdrvotgcnvhzhchzvzevzwkzujgstrksfnejekqdcehiywcxrwydqwptsuftbqryzsrekvjrozttpxvvujkbxwmsyamfxufcnwlirfagrfbymxmfhsupbvpldbizcnveqmnitoadgqrhljiqacnoxrokolhmfaqtjhvtufzidyqmilleiqomqhobjabvdmczcrelabvpedgthenspdwplpclwgtarwwnxcnknyombsxasuzvnaufxecambnobvnfmdbiuvwawyjtrvbqpvbkkiyftwhppymcbkeghjsbgtomzcbsfcbeabtsikvmjlrgmguhyglncicoheoavqywgzgdmsodcbovstylcbmwxiawinjjyoqfwskdgiekxhxigofgihgxqthmefxspekzygwlwszgwxpjhwlxgrkqtcfpddghuhbarprbgfqtzzjmzherfagqeevooxjoodmbmmrdzdoxorasqhmrtdwbqqxerqjijgwjiyhoandbzmvsyyxshxshcggaaeenmpcsgvfrvcgltlwklvdwtmzfrjuvzpyzmotkvhzpwdsghrwwljzwinalcsaaadmjyprofmvxrehognjlfjqgfsbjapppawhvtmczgnreiykgiyfpooalujmeyiwmmyvvyiirsowphijtkgjbcswjfscftqrbpplelqjefxrcvkwhrfowloddqjiraizvibyybtwhdwkcurltzfugeluivcmhcftkjlopllvxohkgyiycecouocqjrqegepvkxkntxgfccjnhxqtpxwiniiconybjdkpyepfiiimu',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.longestPalindromeSubseq(s)
    print(f'r = {r}')
    print('========================')

