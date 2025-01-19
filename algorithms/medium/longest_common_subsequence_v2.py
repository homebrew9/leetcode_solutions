#
# This is Tabulation DP that follows the logic of v1 very closely. No need to set recursion limit here!
#

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)
        grid = [[None for _ in range(N)] for _ in range(M)]
        grid[M-1][N-1] = 1 if text1[N-1] == text2[M-1] else 0
        for c in range(N-2, -1, -1):
            if text1[c] == text2[M-1]:
                grid[M-1][c] = 1
            else:
                grid[M-1][c] = max(grid[M-1][c+1], 0)
        for r in range(M-2, -1, -1):
            if text1[N-1] == text2[r]:
                grid[r][N-1] = 1
            else:
                grid[r][N-1] = max(0, grid[r+1][N-1])
        for r in range(M-2, -1, -1):
            for c in range(N-2, -1, -1):
                if text1[c] == text2[r]:
                    grid[r][c] = 1 + grid[r+1][c+1]
                else:
                    grid[r][c] = max(grid[r][c+1], grid[r+1][c])
        return grid[0][0]


# Main section
for text1, text2 in [
                       ('abc', 'def'),
                       ('abc', 'abc'),
                       ('abcde', 'ace'),
                       ('xastbcmde', 'abmaxcpqe'),
                       ('uwljhevfbr', 'cdltnmznhg'),
                       ('sfivcltxwhgmwepuswvkeicddvpaeweijdtxtwydxjxarawwatzbyogpchvggignxkkbubgxkwdinxerlxezoolamqmsvkbjlrql', 'wtjsrgeheytkhwqyazglqoxcjgkgetbpxykkvjpkhdwwiwxwqmlzrsajratofonjrexkduwkpofdhlqhwjvsocilfthcleloqwhh'),
                       ('qidjjfrvmotajfpuocisuzcmzzpmlyyjrnjvfbzgerurrhjliovcnlloikttjmcrzagkylbtekewopumcrehhmmqvgatezcmieaolwebvtscaotcdcwdkjqkoakkaskygbpmamvylwgpkaasapwezdbkvftrpsjfwzzqntgodajmjzdygmwaukjyklvmkxddjnjbxalmcxyzbaaciwrwryujtpoaytpktotideneepwyztetxemmxumuonpwbklccshasytdukgfrycoyxozwjoxngxdxahutruzworpihwvrzwmjenhqnajclrgeuvzfhxqbemwjfyrihxeixcuwvbfyayhtircptezahuwnrixmqqhspyrismyaootvhfxgagowgxndhwerdabwbabbjtmfoqfjnvehpdkiqugtfielqsrtavtiafeejypbwvnzdsvjtkoafyinqajekmdcxoawzejgppjtsltmbopumjjtthcmgfezcywjxptgmrpkkxbcknqayvsapuvuygotuigzjdodmepawyilmvdpuwcptffsloggotonablxlpvwbljgxxjtqekfhkijlsjadooxcgieuewgdlrpdtcluymlpcqgvvbjbkhwtzdxuxkacwiilpnpwenugcukhryanjsmxilfooertaxddsvuimchjmssbjpkaefwipdduwupalsojqdhfinjdueeghsyyzibpwpuiksqqwwrluoufevvyeercbzdqreqyfzkqxxfisagofsamkcardmpgzcbkjuaaxxozbxujdenrvsdelulrpbskhpvlutyzvfoagzerasitfckwfisqfgymjqpxaojcbotbzmruvrsrnxfbkzfisjplwlubrbcddnmdhpptcjgnomxjknjxisfpocnfkhjflzmyotngzlhfydrolohwehcsxrpzgwsyouwitvtsdmfqecllgfahodwfvigblpsofdkymvemsyixsv', 'tsvymbiwkuaybzdpnbzmzvyiqlqqdyaiaaxdavpisosvjzrldfcqquexwumfrtgzxlbtckzfmfnkiykfscmusldecfcatvcuuzonglnkewrqzwjqfiovmknpzbiqaxztzbaeuamhnzacirslucxqyahhzjnphpmglmqbjalrfypgyuudroffiudrnuemkgrgqakuqcldnocgvlggncrgflbktrudreatuiviewdeopnuhuucubjfxeoxnamwflgavkcymffhssdrnlxgwmavvezclvthxerioeklcgbrfphfawngwnhwhactjeldzyskhkfgvwydngleotmhiefttjkrqprqvvnirdlbfrlfsftttmcpiqtvpdnnafvqvgkenmpabjfdhgccjnvkiawmjljutnblpokjesiqjjpdbdfthssvvpkdrjpvhpamsoknzfriouqnioratfwdjbydawdmkyiztgprupykimbhsqhyugshvaxgpozegahlechwfcmbcpxvkamloygridikyznxzhwfphrxguginbthowduolayaqfcvohwkxxprfjfmjiyleojrmdgmgmfjihtpjueiaqtckfzsbopjwklozmgewvqfdhyfmjjbjgbvcugzgrnrbnoftizrztbgwyyzdfanukpbixtdyheobicpzmsuuwglghvpdmujuesvvwmcxqsmyqgsunqrehcpeldlykcztumdihytfmztdihvnrmtuewbzdchvpzrgusdhrscfuwjagetavzqroypumwjgbidjxiwavhkiotgplvrpkenricnliaypgymsswpydtagbkegiezmkrggldfrmwiqctrfffrfdlcjnrafkbkpfixqmbopxndzweumhsdcyhntnwgciazmdohoelxyfinodlqbpyrgzjnrxkrhulyugmglyfpwcvmywnyoqlltryapvfhfqxepejcnkmeiognjafcqpuxhnvixgqedrh'),
                    ]:
    print(f'text1 = {text1}')
    print(f'text2 = {text2}')
    sol = Solution()
    r = sol.longestCommonSubsequence(text1, text2)
    print(f'r = {r}')
    print('================')


