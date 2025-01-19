package main

import "fmt"

func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}

func longestCommonPrefix(strs []string) string {
    N := len(strs)
    res := strs[0]
    if res == "" {
        return res
    }
    for i := 1; i < N; i++ {
        str := strs[i]
        tmp := ""
        for j := 0; j < min(len(str), len(res)); j++ {
            if str[j] == res[j] {
                tmp += string(str[j])
            } else {
                break
            }
        }
        res = tmp
        if res == "" {
            return res
        }
    }
    return res
}

func main() {
    data := [][]string {
               []string{"flower","flow","flight"},
               []string{"dog","racecar","car"},
               []string{"aaa","aa","aaa"},
               []string{"a"},
               []string{""},
            }
    for _, strs := range data {
        fmt.Printf("strs = %v\n", strs)
        r := longestCommonPrefix(strs)
        fmt.Printf("r = %s\n", r)
        fmt.Println("======================")
    }
}


