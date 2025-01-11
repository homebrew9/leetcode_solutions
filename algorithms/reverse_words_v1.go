package main

import (
    "fmt"
)

func reverseChars (s string, left int, right int) string {
    r := []rune(s)
    for (left < right) {
        temp := r[left]
        r[left] = r[right]
        r[right] = temp
        left++
        right--
    }
    return string(r) 
}

func reverseWords(s string) string {
    passedFirstWord := false
    arr := []string{}
    var left, right int
    for i, v := range s {
        if (v == ' ') {
            continue
        }
        if (i == 0 || s[i-1] == ' ') {
            if (! passedFirstWord) {
                passedFirstWord = true
            } else {
                //fmt.Printf("\t%s\n", s[left:right+1])
                arr = append(arr, s[left:right+1])
            }
            left = i
        }
        right = i
        //fmt.Printf("[%2d] => [%c] ; (l,r) = (%2d,%2d)\n", i, v, left, right)
    }
    //fmt.Printf("\t%s\n", s[left:right+1])
    arr = append(arr, s[left:right+1])
    //for i, v := range arr {
    //    fmt.Printf("\t>>>> [%2d] => [%s]\n", i, v)
    //}
    ret := ""
    for i := len(arr)-1; i >= 0; i-- {
        if ret == "" {
            ret += arr[i]
        } else {
            ret += " " + arr[i]
        }
    }
    //fmt.Println(ret)
    return ret
}

func main() {
    // An additional requirement is to trim leading/trailing spaces and
    // purge in-between spaces to one
    s := []string {
                     "the sky is blue",
                     "  hello world  ",
                     "a good   example",
                     "  Bob    Loves  Alice   ",
                     "Alice does not even like bob",
                     "    Bob   loves      Alice   ",
                     "   A   difficult  C   ",
                     "A   B  C   ",
                     "   abc     def   ghi   jkl   mno    ",
                  }
    var ret string
    for _, v := range s {
        fmt.Printf("Original string = [%s]\n", v)
        ret = reverseWords(v)
        fmt.Printf("Modified string = [%s]\n", ret)
        fmt.Println("=====")
    }
}


