package main

import (
        "fmt"
        "sort"
)

func checkIfCanBreak(s1 string, s2 string) bool {
    arr1 := []int{}
    for _, v := range s1 {
        arr1 = append(arr1, int(v))
    }
    sort.Ints(arr1)
    arr2 := []int{}
    for _, v := range s2 {
        arr2 = append(arr2, int(v))
    }
    sort.Ints(arr2)
    cb1, cb2 := true, true
    for i := 0; i < len(s1); i++ {
        cb1 = cb1 && arr1[i] >= arr2[i]
        cb2 = cb2 && arr2[i] >= arr1[i]
    }
    return cb1 || cb2
}

func main() {
    data := [][]string{
                []string{"abc", "xya"},
                []string{"abe", "acd"},
                []string{"leetcodee", "interview"},
                []string{"mumesxoosf", "krlwrpzneb"},
                []string{"lgwipivkjpnqjncxuaaeiqhlikoypbrilouwqnegkkhurtccwfeeqdttcxlojzvltczuawpjkpudoxvtjqdaxtjinjkcxmlupyfa", "gqelahfdvwilykowkvpqgotcerhhfdsgxvzzwqqmauhanzuwpymgstidpptazyflcnixasesuavqftjncdcwafzgbubsbwrwpzmm"},
                []string{"zrxjnkocvoqkwysqcclzbqmaojngaiohizahztfyhctarpnobizdvgainnzrlifalfpbgzzcqcpjdauwjnqfpwuteapivythljuosiwwhlecouxficbwqlcvbqudnabhxjisppzepyjfxcnvqhmfhcxewdmwpzboadzfzhrxhcsxvnxwttwquiaukpstiorecjitrqxrvusobyywolzcdnswxtkfcwivvymrywkjnwhivnmaxnzduegvzjsvhdgwgpvjdngmjympwssilqhtpfpuxcbbmqfstddlqyaduwshwoctjqawxyvqwyrfojghxvfqahkrqjtzwcymhhcptcnpuursyfiblezevrecjhjcuwazdnmmamvvbywxmldplehozxgvgvzzdspolorehymztmaxvtqkotassdgkpkjazeskmflemebmodohtumnvbsbczquupyvpvpyorhluleadlxugduslqpitlhvkiuvxmmkqvvgpwghgrkiyniutkyvpuvxqpphgsqqvuwojuyptkvriyhyjukkaipnjlqkenlapzzaqgzbsxdgkklibgoyqqzuadlzjzyljkqcwqqmtxcwpsicqmcjvmfdwgdlqcmbmhgpnmxweojfbmqidfbrjwjahbeizyrtihvwalifizrwpcfgsjytpiipmxyldkuhnukdwyfsscanunfzisfnbadbenkdllxwkvsumkxjmkqqlxdeahwngeqivnsbefeuvqevinjotbruaterhwaciqltbyoipkpivklchyxjsstasymjlcnmvyzktcoowrnyubvmcnvclpktxfwcnsovoyhgjvhrbzyrmiotykqhhhhdcnuwuyxwaomqsfiadlzlmqxkokrcpyckimameihjejkeqpizzdkhsukdsxqazvoarjkhogrpejpugpexfrjfazmvryzuqydtmorwrwgoqqofspdsmmgigvlihoyxaeuwbkvkcdvfqpxm", "ljbhqpixqarpxwlfdbamrnjbhrtxjtyrwntdatpudvhcdwlqjmtsvedemkqkanvewnruzqqegaxzagbnktqwrxgdbopobdyflkevfavnghhygweljmptvtbintxllvqzpwhjsienrpxctyyruikwjcxmmothscuowmpavytbxnknkuqsivioncmpiwbonuvoorwmzzkvqlkagaimrhbqmxumsvpqlzglpytpxeglkeuzocgtriterqypjkkogujuhzjpkbtopiixgbcciptevoncylihbjjkwftzrerwzatkedlpespelaxhdfngadboxzgsozwlmkdzgttiaaitvkhqamshvxpohnovyycbfdjleaclllwnbaezjsemynfjfffqvuyduboouxmagryhghklvnbxugyabjanvcyraqysqmtxxgfhlnjexiowxcefxdeopvzlzcwxwvnjytnbzhtsamdvvnevuqzjhisrikklxkhnnvvtfprkiqagmjoqzrlobgpclhwxfzoewsuyudidlqgpcfgropyraowysiyvpsylabcujcwpfmpznmprpqqlircfndeegmxtcfsrhqvapgbxwlwtjmnznllxzwoyyoltpezhlsoqlidhdrooxjaazfzzbvwrsmwrahpevcqqamobpysjhwvwxhgprrechefoxaeenjpcfqzdhjwhcgnjouirmlualziygmzakldgdffyxpzlahabtwynbpuhjdgyateevqbrketeusxtamqahiqdxxtvoqwsqqtymuvblkoleunqnomrhaovynjhffhvxosoqftnoihieocxirccwmenqhyyxahepmoqzuqegcjrbwfysjanwjjcjrlwmpmhbkhtdyevbpquuxwrldbqzbmjnvfkhynkoekccdspieznajtplvinmnneufikadohiwgaspvzfhljvzswbnpnbpnwomqhxsnnfckpfdizoirjavsujdxfzlhy"},
            }
    for _, v := range data {
        s1, s2 := v[0], v[1]
        fmt.Printf("s1, s2 = %s, %s\n", s1, s2)
        r := checkIfCanBreak(s1, s2)
        fmt.Printf("r = %v\n", r)
        fmt.Println("=================")
    }
}


