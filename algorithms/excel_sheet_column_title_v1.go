package main

import "fmt"

func convertToTitle(columnNumber int) string {
    hsh := make(map[int]int)
    for i := 0; i < 26; i++ {
        hsh[i+1] = i + 65
    }
    var arr []int
    hi := -1
    for columnNumber > 0 {
        q := columnNumber / 26
        r := columnNumber % 26
        if r == 0 {
            q -= 1
            r = 26
        }
        arr = append(arr, hsh[r])
        hi++
        columnNumber = q
    }
    //fmt.Println(hi)
    //fmt.Println(arr)
    ret := ""
    for hi >= 0 {
        ret += string(arr[hi])
        hi--
    }
    return ret
}

func main() {
    arr := []int{
               1,
               28,
               696,
               697,
               698,
               699,
               700,
               701,
               702,
               703,
               704,
               705,
               706,
               707,
               3481,
               2147483647,
           }
    for _, v := range arr {
        ret := convertToTitle(v)
        fmt.Println("columnNumber = ", v)
        fmt.Println("ret          = ", ret)
        fmt.Println("=======================")
    }
}

