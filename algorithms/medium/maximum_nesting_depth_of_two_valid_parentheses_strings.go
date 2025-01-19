// It's difficult to figure out what the problem wants us to do, initially. But pay
// attention to the word "subsequence". We simply need to create two subsequences so
// that they have the least nesting depth. Subsequences preserve the order.
// Also check the solutions by Domii and lee215.

package main

import "fmt"

func maxDepthAfterSplit(seq string) []int {
    stack := []int{}
    res := []int{}
    curr := 0
    for _, ch := range seq {
        if ch == '(' {
            if len(stack) > 0 {
                curr = (stack[len(stack)-1] + 1) % 2
            }
            stack = append(stack, curr)
            res = append(res, curr)
        } else {
            prev := stack[len(stack) - 1]
            stack = stack[:len(stack)-1]
            res = append(res, prev)
        }
    }
    return res
}

func main() {
    data := []string{
                "(()())",
                "()(())()",
                "(((()())))",
                "()()()()()()()()",
                "()()()()(())()(()()((())))",
            }
    for _, seq := range data {
        fmt.Printf("seq = %s\n", seq)
        r := maxDepthAfterSplit(seq)
        fmt.Printf("r   = %v\n", r)
        fmt.Println("===================")
    }
}


