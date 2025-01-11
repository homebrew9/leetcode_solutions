#
# DP : Iterative, tabulation
#
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        #print(f'dp = {dp}')
        return dp[0][N-1]

# Main section
for s in [
            'bbbab',
            'cbbd',
            'vgpfhgdxfl',
            'upvgarvtptjnjkbtusgskremmcmnkfnajkuloydxevabqsgvtqoovgbolsoiddqwjuuqgejfcvykorsybarsbcacnpoicsrqkwqr',
            'onibfnbkjdgpzfhxmwmamrosuulkovspjharpntwkjuvjzbjwrnykwvdfurnxkuuemmyxavkeowloobdgmpbxczuufgtmkcoqeqcyentbofyamtbzoklwmwxeeoicghvflguogmzbnevemnqacpsjeneepozkuqmgpqinhjyclifmxuuvnmhieyhlqcmfvifeyzjbmmnenfexedoeznaghvshlcwhigqcuxsgodwtbmhfbyrfydsbivfdzgjxveynrntlnwjdswxneksffkzdxrtmlltkrxxbsxskwjzouxqdyauklvsbbxawmdrbmytigvpfvoituonpwzlspyuliyaaepxklpeqledgfjlxbkhjdxuuekxxbpqkpznpziatwtmmrkltycyxfbbofothmyofkycaswcrphrrrndxrnkzmeumsdtpxunjrkyxnjutrbzmvxvajgnpwimvabjaxmvuamjkfapxsgdfihozwojazlnhgyj',
            'ayddhbqpytgiarzbaxwsgwqmjtyybmvcfdwnrmgqwqwvntgnvuxhfbowwrftqyjedudlmfeiunoqhoushzmfornepqykteusfkajlczippkqvlsspytiiwktvzwubkubrvdkvwzinkcnlkhmqhuhdkttdmmwhfebqhwsqnfauhbtktjalstdrvotgcnvhzhchzvzevzwkzujgstrksfnejekqdcehiywcxrwydqwptsuftbqryzsrekvjrozttpxvvujkbxwmsyamfxufcnwlirfagrfbymxmfhsupbvpldbizcnveqmnitoadgqrhljiqacnoxrokolhmfaqtjhvtufzidyqmilleiqomqhobjabvdmczcrelabvpedgthenspdwplpclwgtarwwnxcnknyombsxasuzvnaufxecambnobvnfmdbiuvwawyjtrvbqpvbkkiyftwhppymcbkeghjsbgtomzcbsfcbeabtsikvmjlrgmguhyglncicoheoavqywgzgdmsodcbovstylcbmwxiawinjjyoqfwskdgiekxhxigofgihgxqthmefxspekzygwlwszgwxpjhwlxgrkqtcfpddghuhbarprbgfqtzzjmzherfagqeevooxjoodmbmmrdzdoxorasqhmrtdwbqqxerqjijgwjiyhoandbzmvsyyxshxshcggaaeenmpcsgvfrvcgltlwklvdwtmzfrjuvzpyzmotkvhzpwdsghrwwljzwinalcsaaadmjyprofmvxrehognjlfjqgfsbjapppawhvtmczgnreiykgiyfpooalujmeyiwmmyvvyiirsowphijtkgjbcswjfscftqrbpplelqjefxrcvkwhrfowloddqjiraizvibyybtwhdwkcurltzfugeluivcmhcftkjlopllvxohkgyiycecouocqjrqegepvkxkntxgfccjnhxqtpxwiniiconybjdkpyepfiiimu',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.longestPalindromeSubseq(s)
    print(f'r = {r}')
    print('========================')


