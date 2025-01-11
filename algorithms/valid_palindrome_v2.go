package main

import "fmt"

func isPalindrome(s string) bool {
    var arr []int
    isPalindrome := true
    right := -1
    for _, c := range s {
        if 'a' <= c && c <= 'z' {
            arr = append(arr, int(c))
            right++
        }
        if 'A' <= c && c <= 'Z' {
            arr = append(arr, int('a'+c-'A'))
            right++
        }
        if '0' <= c && c <= '9' {
            arr = append(arr, int(c))
            right++
        }
    }
    //fmt.Printf("arr = %v ; right = %d\n", arr, right)
    for left := 0; left < right; left, right = left+1, right-1 {
        if arr[left] != arr[right] {
            //fmt.Println("string is NOT a palindrome!")
            isPalindrome = false
            break
        }
    }
    return isPalindrome
}

func main() {
    arr := []string {
               "A man, a plan, a canal: Panama!",
               "race a car",
               " ",
               "race-car",
               "hello911 abba 119olleh ",
               "malayalam",
               "--*!& redivider 1221 redivider #$%^+_{} redivider 1221 redivider !!@#()",
               "the woods are lovely, dark and deep",
               ".,",
               "~!@#$%^&  *()_+=-{}[]",
               "~",
               "~!@#$%^&W *()_+=-{}[]",
               "~!@#$%^&  *()_+=-{}[W",
               "W!@#$%^&  *()_+=-{}[]",
               "",
           }
    for _, v := range arr {
        fmt.Printf("s = [%v]\n", v)
        r := isPalindrome(v)
        fmt.Println(r)
        fmt.Println("======================")
    }
}

