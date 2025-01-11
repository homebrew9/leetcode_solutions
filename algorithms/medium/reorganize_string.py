'''
767. Reorganize String
Medium

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"

Example 2:

Input: s = "aaab"
Output: ""

Constraints:

    1 <= s.length <= 500
    s consists of lowercase English letters.
'''
# ======================================================

from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        N = len(s)
        cntr = Counter(s)
        res = [None for _ in range(N)]
        keys = [p[0] for p in sorted([(k, v) for k, v in cntr.items()], key=lambda x: -x[1])]
        j = 0
        for i in range(0, N, 2):
            while cntr[keys[j]] == 0:
                j += 1
            res[i] = keys[j]
            cntr[keys[j]] -= 1
        j = 0
        for i in range(1, N, 2):
            while cntr[keys[j]] == 0:
                j += 1
            res[i] = keys[j]
            cntr[keys[j]] -= 1
        for i in range(1, N):
            if res[i] == res[i-1]:
                return ''
        return ''.join(res)


# Main section
for s in [
            'aaaaabbbbcccddefg',
            'aaab',
            'aab',
            'x',
            'xyz',
            'xyy',
            'zzz',
            'yutuxqjnvxkavcxaphxkcqkkkjvoioicfeumrbmvblhgrjdrmp',
            'ognnhrjbfppwaonzpjfcdqrspcwizekouqvwvtledtsmtlmifsgosmpvuoesjygtrsvejxxcqsqqzjwbwxbxbfmodlwynvaplntr',
            'cwemstjkxupapxacwebskoisuagwdvxczzxhympcfbwxzfscekahmltrcwkwnlhranzsgiohdvgyxafpnlkbmrsycznrqdelwboniiiifegseyyliyfugvdihqzrcvpetnzuowxzpjswjoasaquhzalowgyuhsutusaxanrwhhwmnlpodfgasivtcmjrbfxmcgwprgaf',
            'ryzphhryharkwgilnxjcbzambdsvfzfwjvxbjnndrcdstnrlklibvzrvwnwwhydrfsyxqwjlhowyfgvsydbjfgrbvvhnqcboraivsthcyvwayrlnewtnadcyucenskelhrzwobotjekzkoidusanzrleggtyesiwtevihjpknhrotfvmwvlorbnmwvdvburwwppbedffeuwcttcoqbuismkytgmzrcpqqtkmbuaqjdmjrdsawicyuhhpox',
            'syzmlqmkofhrlfgyoxgafyidnwzsrlplzxrpyyhnooejflequxzfkcjpadaokjdajqgjxwwuiisgnlimvyuzilztdmmipcxyjuxdmpkzdvzglcwsauybghvloxktliqxzjvqbgixismlxnmiqwlsutpuxbfqiitohspayjkqpujnqzyolelfgvxoywbctqiuemwaixgwcfsuakkfrfabmtqaanowzhmjvfpbvxhkwbsovocgjlqqisetojhtbyulqtrmxxwuxkzietqmyulrjydueslwspkfxmflimpkirht',
            'isheoiudqsioffcgobtltgbwciiekvjeqapaxctmldbjvcrznpncbhszstzewoktjvnaogrjcsterytnsgllbxoymttpjyixkfgifuptibvupvvgfadalijfgqrrdmwwccybgzojfkwtwrnbobpghiciwujgkfgdawyzbpoqldbbnynvnsjcucqsoljpbczywlysoczctswfmbnperfvnsemdjtarvqqsmwgvricydwwnuwziwdyygibuqqxtjyhxvmrdetlrrpiovemredytxcnrhtnnekxppngcxqvedyremvclqvpdzppvydmetddqhpzcsadvttojgwjjzkarkgeijnzjgrmavhsumbneahvhyfalzdvulykcifvzingnozsfebnfajiyygp',
            'cpkfdelacsxvufvwavwwbmkwzxssemjabqbrobwiqeiemungpdygmdwzdbmoraaakynyoqbezpylfrnrpundhysoclakqqorgxejohebhqunjmfzsfmoklgiimtxuqxsqbflrmwuokxiovmehbzegwwnxypivtnptpfbffgjqovjlbeumqqhyltjjulugxgnonovwifshbmbtzebmiyaoahdvqpzmkpwwlxqzhihdqdtrxlegevncyaawsyueacosdibxvgzrnbxkvhfeiqydynusonahpypagfgagxxinlvmitqujjifmhgtsauodmejswqhycwzdkftirzawizquzitvuamvddoqlfrmmvhzplxfgqztylbrqyhmfvpltixnfbzrmyhtfsqwwzdifihplxjonpehwlbmwhaxtlyjoqzzcyjswawfrmphxcylrenbyakswnzhzkrbqzmdhihtcgxpssyjcesegtjncxlodvhcnkctne',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.reorganizeString(s)
    print(f'r = {r}')
    if len(r) > 0:
        assert(Counter(s) == Counter(r))
    print('=========================')


