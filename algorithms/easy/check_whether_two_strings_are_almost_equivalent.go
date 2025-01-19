package main

import "fmt"

func abs(x int) int {
    if x >= 0 {
        return x
    }
    return -x
}
func checkAlmostEquivalent(word1 string, word2 string) bool {
    cntr1 := make(map[rune]int)
    cntr2 := make(map[rune]int)
    for _, v := range word1 {
        cntr1[v]++
    }
    for _, v := range word2 {
        cntr2[v]++
    }
    //fmt.Println(cntr1)
    //fmt.Println(cntr2)
    for k, v := range cntr1 {
        v1, ok := cntr2[k]
        //fmt.Println(k, v, v1, ok, abs(v - v1))
        if ok && abs(v - v1) > 3 {
            return false
        } else if !ok && v > 3 {
            return false
        }
    }
    //fmt.Println("=============")
    for k, v := range cntr2 {
        v1, ok := cntr1[k]
        //fmt.Println(k, v, v1, ok, abs(v - v1))
        if ok && abs(v - v1) > 3 {
            //fmt.Println("inside if ok && cond1...")
            return false
        } else if !ok && v > 3 {
            //fmt.Println("inside else if v > 3")
            return false
        }
    }
    return true
}

func main() {
    data := [][]string {
                []string{"aaaa", "bccb"},
                []string{"abcdeef", "abaaacc"},
                []string{"cccddabba", "babababab"},
                []string{"aaaa", "aaaa"},
            }
    for _, v := range data {
        word1, word2 := v[0], v[1]
        fmt.Printf("word1, word2 = %s, %s\n", word1, word2)
        r := checkAlmostEquivalent(word1, word2)
        fmt.Printf("r = %v\n", r)
        fmt.Println("==================")
    }
}


