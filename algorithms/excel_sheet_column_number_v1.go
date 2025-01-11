package main

import "fmt"

func titleToNumber(columnTitle string) int {
    size := len(columnTitle)
    pv := 1
    ret := 0
    for i, _ := range columnTitle {
        v := columnTitle[size-i-1]
        //fmt.Printf("%c %d\n", v, v)
        //fmt.Printf("\t>>> num = [%d]\n", int(v)-'A')
        ret += (int(v) - 'A' + 1) * pv
        pv *= 26
    }
    return ret
}

func main() {
    arr := []string{
               "A",
               "B",
               "C",
               "X",
               "Y",
               "Z",
               "AA",
               "AB",
               "ZT",
               "ZU",
               "ZV",
               "ZW",
               "ZX",
               "ZY",
               "ZZ",
               "AAA",
               "AAB",
               "AAC",
               "AAD",
               "AAE",
               "ECW",
               "FXSHRXW",
           }
    for _, v := range arr {
        fmt.Println(v)
        r := titleToNumber(v)
        fmt.Println(r)
        fmt.Println("===================================")
    }
}

