package main

import (
    "fmt"
)

func reverse_chars (s string, left int, right int) string {
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

func reverse_words(s string) string {
    var left, right, size int
    left, right, size = 0, 0, 0
    for i, v := range s {
        //fmt.Printf("\t[%d] : [%c]\n", i, v)
        if (v == ' ') {
            right = i - 1
            //fmt.Printf("\t\treverse the word now! (left, right) = (%d,%d)\n", left, right)
            s = reverse_chars(s, left, right)
            left = i + 1
        }
        size++
    }
    //fmt.Printf("\t\treverse the word now! (left, right) = (%d,%d)\n", left, size-1)
    s = reverse_chars(s, left, size-1)
    s = reverse_chars(s, 0, size-1)
    return s
}

func main() {
    s := []string {
                     "the sky is blue",
                     "  hello world  ",
                     "a good   example",
                     "  Bob    Loves  Alice   ",
                     "Alice does not even like bob",
                  }
    var ret string
    for _, v := range s {
        fmt.Printf("Original string = [%s]\n", v)
        ret = reverse_words(v)
        fmt.Printf("Modified string = [%s]\n", ret)
        fmt.Println("=====")
    }
}

