/*
You are given a string s consisting of lowercase English letters. A duplicate
removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can
be proven that the answer is unique.
E.g. "abbaca" => "ca"
     "azxxzy" => "ay"
*/
package main

import (
    "fmt"
)

func top(stack []rune) rune {
    // stack should have at least one element!
    return stack[len(stack)-1]
}

func push(stack []rune, r rune) []rune {
    stack = append(stack, r)
    return stack
}

func pop(stack []rune) []rune {
    return stack[:len(stack)-1]
}

func removeDuplicates(s string) string {
    var stack []rune
    for i, v := range s {
        //fmt.Printf("i, v, stack = %d, %c, %v\n", i, v, stack)
        if i == 0 {
            stack = push(stack, v)
        } else if len(stack) > 0 && v == top(stack) {
            stack = pop(stack)
        } else {
            stack = push(stack, v)
        }
    }
    return string(stack)
}

func main() {
    //s := "bcbaa"
    //fmt.Println("Original : ", s)
    //fmt.Println("========================")
    //s = removeDuplicates(s)
    //fmt.Println("========================")
    //fmt.Println("Modified : ", s)
    arr := []string {
               "abbaca",
               "azxxzy",
               "aaaaa",
               "aaaa",
               "",
               "a",
               "aa",
               "ab",
               "aabcb",
               "aabcbaa",
               "bcbaa",
               "abcdefedcba",
               "abcdeffedcxx",
               "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",
               "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba",
           }
    for _, v := range arr {
        fmt.Printf("Original : [%s]\n", v)
        fmt.Printf("Modified : [%s]\n", removeDuplicates(v))
        fmt.Println("===========")
    }
}


