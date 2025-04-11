package main

import "fmt"

func longestCommonPrefix(s string, t string) int {
	N := len(s)
	M := len(t)
	res := 0
	skip := 0
	i, j := 0, 0
	for i < N && j < M {
		if s[i] != t[j] {
			if skip < 1 {
				skip += 1
				i++
			} else {
				return res
			}
		} else {
			res++
			i++
			j++
		}
	}
	return res
}

func main() {
	data := [][]string{
		[]string{"madxa", "madam"},
		[]string{"leetcode", "eetcode"},
		[]string{"one", "one"},
		[]string{"a", "b"},
	}
	for _, v := range data {
		s, t := v[0], v[1]
		fmt.Printf("s, t = %s, %s\n", s, t)
		r := longestCommonPrefix(s, t)
		fmt.Printf("r = %d\n", r)
		fmt.Println("========================")
	}
}
