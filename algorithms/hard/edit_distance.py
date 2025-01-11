class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        E = [[None for _ in range(N+1)] for _ in range(M+1)]
        E[0][0] = 0
        for i in range(N):
            E[0][i+1] = i + 1
        for i in range(M):
            E[i+1][0] = i + 1
        #print(f'\tE = {E}')
        for i in range(M):
            for j in range(N):
                #print(f'\t\t(i, j) = ({i}, {j}) => E[{i+1}][{j+1}]')
                E[i+1][j+1] = min(E[i+1][j]+1, E[i][j+1]+1, E[i][j] + (1 if word2[i] != word1[j] else 0))
        return E[M][N]
       
# Main section
for word1, word2 in [
                       ('horse', 'ros'),
                       ('intention', 'execution'),
                       ('snowy', 'sunny'),
                       ('polynomial', 'exponential'),
                       ('exponential', 'polynomial'),
                       ('x', ''),
                       ('', 'x'),
                       ('a', 'b'),
                       ('xneyceqsoksmzbtyamzvzfnmfpbqorynlntohbweywwtmozbslttyptrvzbttualocfmjkwhuhlnnghyxbbkxswnnvijxoutsaqgzdevdaohlucbitxofifpgpxbtepwkabbogawepobnlmvaifxebwllbcrfdugzpeevurajmxnieloszkczlyjkozsrchgdzvfqxrlkvdtrbdvroceenzdevferoclolegiexxekjcbgpyomqernxkoulxfzznhktywufyfrbijbyaedskquhmkcteukwxgcihthokyovujzihmwsochdujthhbvmmdgcymwiuyzpotxkhjbyulodektegugcqocouongrtxpabkwadfckybpzgtbwgvevnmywrpqvpmhvlizglyibrsimgjcnsxldeiuimxfnpyrayzxavlmzroelanuczmfcwdsnnoicduutqrxtkceoxvcwgmlkrggsmcrbtrbgurexpwlghcaf', 'czzpqvkynpphtkmsvdllpgdxghzjpkgmtyvflryachkpcvrqiqvbtooyrpfdysrsafxvcnjtmjnhedikktgqaxlwigrvdpwqqdenkztbfenxlvpmmdbimjcdzuzausewbljvodvczxvcmdqqoblcfmxfqcdcorkgrthdsnkaupbhtfndfsdzxyqohlnyfggryuabcyywkegbhqumibnovojyeitzkvwwmwhzqymqfukaghlqndbkkwvveinbevgjamypuvgmsvyxlbyrmufnzmgzrgdsqicpikyeqgtbcplyqzckcdmhnhwermlavhwjwwfisaxgfaxosnwgrwmspvrxtpjvwmpvdowcgpiwgfbobluxavkztyajlhysoavjynmzfyvppkzsqodnumxibrkreqeapdcsuwtmvbqzpsxzsvdwvuqvsbdguklabgwdauhemnbyajfcvqnzantlczhzgfzeyqqddukvsqgasquhsnbofbjd'),
                       ('qxsxolgeikxjawxvlgknifmvdeidykwarhvhlnpjobviscixwxvfnogiiutdgqzudbxlwdqjolfbjdsojdmmolhxaypbfjokibfmwaifxgsukouvsssrerrhfumdsmhexcguvvojbokfasbfmzuihfbveotudilwwyazmkcwirdnljudymnhcfniigxpnchunhjafrzxchtvpqnaflytaltjrtyfhkbagjffureptvctprwqdefsnrscutoxwmyknlatkhpdenkcqzsujmqeuazafvxxksejrqyfccykolafblidtvuxtinxtkmzoymrrajnbplyrynkqsmknjqeemnyhrhxphlalgmjthkoabrdjnerxcaxjxfoqgjwzyvxvwemtngxumwbwyleuvcakltxxhbpvyelaqrxclntgordigpjwyrgomeqospixbqgadercrpmbgdwfqjhgxvzkxslaowcdffwsatxxysksgtvxawdllibzedextteghajohbiubbwlkbwccuydizbbygatdbxnvewajzmixwcfnhkehpxteksafzlsrojqorzblyfgeltwnjstsqufszdcrvgsubydsdlfewoqwjepkgzmoivypqzlarpjzbqlfwqhvqmcqztlyfdorowulnpwpqpirqexzoplcqrxhxrukvufmzblnkvhuwjqmxzeoffvvsrzaosrsfautansqamgthfwlswjzlkhdlvjjopouvtlvoaaikhcvuddsncvvkwfgjoygentoogykihxtkbaipletyioovybipksucvyaodlmfgdeptvvlbvdiqwkeongakuiyvxxhqqyzzjebdaedcwqxsucjonkjbxsmdwsaggewgpcsbftrkxbmryslwmmdiyiwvxdcqyaqvclqlnclpafvpvzyggdlyorihlvgmvxslwkmkhdgrysisyiwpgfgseinkvphyavtnwljmormebkdxgnldunllwrmt', 'gurttpyixalwopkjaalcrtjagkvcbykdvbrywudiulqfhfbzmtvhlxqbwvnpzfunqskrlnkqjpfdrznlkjayuxnwjezkrxhzkmcvzlsqvwsbgouuxppwkyvakkaljfgkqepkfmxysyzmjpgywqbkjvigaybuccixxbqobtxcepfrzilqjccbaqwjzcmqqvzzzsmzkcdppmlgeukdlguhjaifxyczclfyqnxmeebchtrcypneuomdttixntckhwplypczicteplptehepttplqhqlgewewzlvnpaamwsxvedifbrzcjlyylljlclaleukkfvuvczryfgekcvzsnsbexlqrvjtitfngbeswnjcbiphdcukvpcpvopkawnjuthqjrfvazjmkdxdvtptubqxysdkkxpywotrbdzonfjdctqakkgsmzmyghvlnnsmzcbfzjjjuinowcyckxnqvjicxghgqamfflomwsnzecapcgbynnyqjoznutuzhinpxmjlssspzbeznafczfzvibrhoucltdvkookaommuclcvdmvgjfcykssidglewgqoiquxzhcvfiyqzjsgswarirfwacppiogfordadaheicbnllatnzbkwroquqvlusqydqkkkfsklkhpqvdhqpzzwzbaynzsknntbgmwrfzlnopmrytvfzoaoxeoqszdophvcniitfcpnuqatkqnauqqjfpqmqitsztsjnbsrvmyluqlkgbmhejpcuczycpxegaqwiwnbdvdatweruwkrqypeecrbxrqlkvhqlvkocvotvitsuuctnqugxgltukpbmrmblhzkbutduxvdqknnblzirxrdrzfjzbvipdjjgyvlbphnvyojoacbiysygjxfjjfexlkfqruphvdfqankfjqxgchweoxchgynclhvnsqldsmbehgrjrathrhugumfsjckmsaxpaueeyhludxwefwxlznxenquqkkazutidhtwhhj'),
                    ]:
    print(f'word1, word2 = {word1}, {word2}')
    sol = Solution()
    r = sol.minDistance(word1, word2)
    print(f'r = {r}')
    print('==============')

