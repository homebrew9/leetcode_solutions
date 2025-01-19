class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        '''
            s1 = "leetcodee" ; "c d eeee    l   o   t"
            s2 = "interview" ; "    ee   ii   n   r t v w"
            s1 = "c d ee    l   o"
            s2 = "       ii   n   r v w"
        '''
        s1_sorted = ''.join(sorted(s1))
        s2_sorted = ''.join(sorted(s2))
        #can_break = True
        #for x, y in zip(s1_sorted, s2_sorted):
        #    if x < y:
        #        can_break = False
        #if can_break:
        #    return True
        #can_break = True
        #for x, y in zip(s2_sorted, s1_sorted):
        #    if x < y:
        #        can_break = False
        #return can_break
        return all([x >= y for x, y in zip(s1_sorted, s2_sorted)]) or all([x >= y for x, y in zip(s2_sorted, s1_sorted)])

# Main section
for s1, s2 in [
                 ('abc', 'xya'),
                 ('abe', 'acd'),
                 ('leetcodee', 'interview'),
                 ('mumesxoosf', 'krlwrpzneb'),
                 ('lgwipivkjpnqjncxuaaeiqhlikoypbrilouwqnegkkhurtccwfeeqdttcxlojzvltczuawpjkpudoxvtjqdaxtjinjkcxmlupyfa', 'gqelahfdvwilykowkvpqgotcerhhfdsgxvzzwqqmauhanzuwpymgstidpptazyflcnixasesuavqftjncdcwafzgbubsbwrwpzmm'),
                 ('zrxjnkocvoqkwysqcclzbqmaojngaiohizahztfyhctarpnobizdvgainnzrlifalfpbgzzcqcpjdauwjnqfpwuteapivythljuosiwwhlecouxficbwqlcvbqudnabhxjisppzepyjfxcnvqhmfhcxewdmwpzboadzfzhrxhcsxvnxwttwquiaukpstiorecjitrqxrvusobyywolzcdnswxtkfcwivvymrywkjnwhivnmaxnzduegvzjsvhdgwgpvjdngmjympwssilqhtpfpuxcbbmqfstddlqyaduwshwoctjqawxyvqwyrfojghxvfqahkrqjtzwcymhhcptcnpuursyfiblezevrecjhjcuwazdnmmamvvbywxmldplehozxgvgvzzdspolorehymztmaxvtqkotassdgkpkjazeskmflemebmodohtumnvbsbczquupyvpvpyorhluleadlxugduslqpitlhvkiuvxmmkqvvgpwghgrkiyniutkyvpuvxqpphgsqqvuwojuyptkvriyhyjukkaipnjlqkenlapzzaqgzbsxdgkklibgoyqqzuadlzjzyljkqcwqqmtxcwpsicqmcjvmfdwgdlqcmbmhgpnmxweojfbmqidfbrjwjahbeizyrtihvwalifizrwpcfgsjytpiipmxyldkuhnukdwyfsscanunfzisfnbadbenkdllxwkvsumkxjmkqqlxdeahwngeqivnsbefeuvqevinjotbruaterhwaciqltbyoipkpivklchyxjsstasymjlcnmvyzktcoowrnyubvmcnvclpktxfwcnsovoyhgjvhrbzyrmiotykqhhhhdcnuwuyxwaomqsfiadlzlmqxkokrcpyckimameihjejkeqpizzdkhsukdsxqazvoarjkhogrpejpugpexfrjfazmvryzuqydtmorwrwgoqqofspdsmmgigvlihoyxaeuwbkvkcdvfqpxm', 'ljbhqpixqarpxwlfdbamrnjbhrtxjtyrwntdatpudvhcdwlqjmtsvedemkqkanvewnruzqqegaxzagbnktqwrxgdbopobdyflkevfavnghhygweljmptvtbintxllvqzpwhjsienrpxctyyruikwjcxmmothscuowmpavytbxnknkuqsivioncmpiwbonuvoorwmzzkvqlkagaimrhbqmxumsvpqlzglpytpxeglkeuzocgtriterqypjkkogujuhzjpkbtopiixgbcciptevoncylihbjjkwftzrerwzatkedlpespelaxhdfngadboxzgsozwlmkdzgttiaaitvkhqamshvxpohnovyycbfdjleaclllwnbaezjsemynfjfffqvuyduboouxmagryhghklvnbxugyabjanvcyraqysqmtxxgfhlnjexiowxcefxdeopvzlzcwxwvnjytnbzhtsamdvvnevuqzjhisrikklxkhnnvvtfprkiqagmjoqzrlobgpclhwxfzoewsuyudidlqgpcfgropyraowysiyvpsylabcujcwpfmpznmprpqqlircfndeegmxtcfsrhqvapgbxwlwtjmnznllxzwoyyoltpezhlsoqlidhdrooxjaazfzzbvwrsmwrahpevcqqamobpysjhwvwxhgprrechefoxaeenjpcfqzdhjwhcgnjouirmlualziygmzakldgdffyxpzlahabtwynbpuhjdgyateevqbrketeusxtamqahiqdxxtvoqwsqqtymuvblkoleunqnomrhaovynjhffhvxosoqftnoihieocxirccwmenqhyyxahepmoqzuqegcjrbwfysjanwjjcjrlwmpmhbkhtdyevbpquuxwrldbqzbmjnvfkhynkoekccdspieznajtplvinmnneufikadohiwgaspvzfhljvzswbnpnbpnwomqhxsnnfckpfdizoirjavsujdxfzlhy'),
              ]:
    print(f's1, s2 = {s1}, {s2}')
    sol = Solution()
    r = sol.checkIfCanBreak(s1, s2)
    print(f'r = {r}')
    print('==================')


