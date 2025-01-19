package main

import "fmt"

func canBeValid(s string, locked string) bool {
    N := len(s)
    if N % 2 == 1 {
        return false
    }
    openCount := 0
    for i := 0; i < N; i++ {
        ch := s[i]
        lc := locked[i]
        if lc == '0' || ch == '(' {
            openCount++
        } else {
            openCount--
            if openCount < 0 {
                return false
            }
        }
    }
    closedCount := 0
    for i := N - 1; i >= 0; i-- {
        ch := s[i]
        lc := locked[i]
        if lc == '0' || ch == ')' {
            closedCount++
        } else {
            closedCount--
            if closedCount < 0 {
                return false
            }
        }
    }
    return true
}

func main() {
    data := [][]string {
                []string{"))()))"       , "010100"},
                []string{"()()"         , "0000"  },
                []string{")"            , "0"     },
                []string{"))()))"       , "011010"},
                []string{"())(()(()(()" , "100011110110"},
                []string{"()"           , "11"},
                []string{"())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(", "100011110110011011010111100111011101111110000101001101001111"},
            }
    for _, v := range data {
        s, locked := v[0], v[1]
        fmt.Printf("s, locked = %s, %s\n", s, locked)
        r := canBeValid(s, locked)
        fmt.Printf("r = %v\n", r)
        fmt.Println("==================")
    }
}


