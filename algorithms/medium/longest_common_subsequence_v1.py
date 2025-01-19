#
# Note that the Top Down DP throws an "RecursionError: maximum recursion depth exceeded" error in
# my Python system. But it works fine in LC. I can forcibly set the recursion limit to a high
# value and make it work in my system. Just something to keep in mind!
# Uncomment the lines regarding the sys module if you want the 4th testcase to work!
#

import sys
sys.setrecursionlimit(1000000)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def solve(i, j):
            if i >= N or j >= M:
                return 0
            if (i, j) in hsh:
                return hsh[(i, j)]
            if text1[i] == text2[j]:
                tmp = 1 + solve(i+1, j+1)
            else:
                tmp = max(solve(i+1, j), solve(i, j+1))
            hsh[(i, j)] = tmp
            return hsh[(i, j)]
        N = len(text1)
        M = len(text2)
        hsh = dict()
        return solve(0, 0)

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
    print(f'text1 = {text2}')
    sol = Solution()
    r = sol.longestCommonSubsequence(text1, text2)
    print(f'r = {r}')
    print('================')


