package main

import "fmt"

func reverseOnlyLetters(s string) string {
    arr := []string{}
    for _, v := range s {
        if (int(v) >= 65 && int(v) <= 90) || (int(v) >= 97 && int(v) <= 122) {
            arr = append(arr, string(v))
        }
    }
    j := len(arr) - 1
    res := ""
    for _, v := range s {
        if (int(v) >= 65 && int(v) <= 90) || (int(v) >= 97 && int(v) <= 122) {
            res += arr[j]
            j--
        } else {
            res += string(v)
        }
    }
    return res
}

func main() {
    for _, s := range []string {
                                  "ab-cd",
                                  "a-bC-dEf-ghIj",
                                  "Test1ng-Leet=code-Q!",
                               }{
        fmt.Printf("s = %s\n", s)
        r := reverseOnlyLetters(s)
        fmt.Printf("r = %s\n", r)
        fmt.Println("===================")
    }
}


