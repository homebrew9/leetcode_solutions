package main

import "fmt"

func triangleType(nums []int) string {
	a, b, c := nums[0], nums[1], nums[2]
	if !(a+b > c && b+c > a && c+a > b) {
		return "none"
	}
	if a == b && b == c {
		return "equilateral"
	}
	if a == b || b == c || c == a {
		return "isosceles"
	}
	return "scalene"
}

func main() {
	data := [][]int{
		[]int{3, 3, 3},
		[]int{3, 4, 5},
		[]int{4, 5, 5},
		[]int{17, 19, 36},
	}
	for _, nums := range data {
		fmt.Printf("nums = %v\n", nums)
		r := triangleType(nums)
		fmt.Printf("r    = %s\n", r)
		fmt.Println("=====================")
	}
}
