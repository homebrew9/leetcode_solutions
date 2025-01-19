package main

import (
    "fmt"
    "strconv"
)

func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}

func digitSum(s string, k int) string {
    for len(s) > k {
        tmp := ""
        for i := 0; i < len(s); i = i + k {
            chunk := s[i:min(i+k, len(s))]
            sum := 0
            for _, v := range chunk {
                sum += int(v-'0')
            }
            tmp += strconv.Itoa(sum)
        }
        s = tmp
    }
    return s
}

func main() {
    type Pair struct {
        s  string
        k  int
    }
    for _, v := range []Pair {
                               Pair{"11111222223", 3},
                               Pair{"00000000", 3},
                             }{
        fmt.Printf("s = %s ; k = %d\n", v.s, v.k)
        r := digitSum(v.s, v.k)
        fmt.Printf("r = %s\n", r)
        fmt.Println("===================")
    }
}

