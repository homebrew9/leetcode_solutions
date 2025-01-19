package main

import "fmt"

func openLock(deadends []string, target string) int {
    deadendSet := make(map[string]bool)
    for _, v := range deadends {
        deadendSet[v] = true
    }
    start := "0000"
    dq := []string{start}
    seen := make(map[string]bool)
    seen[start] = true
    steps := 0
    for len(dq) > 0 {
        size := len(dq)
        for i := 0; i < size; i++ {
            curr := dq[0]
            dq = dq[1:]
            if curr == target {
                return steps
            }
            _, okDE := deadendSet[curr]
            if !okDE {
                var digit string
                for j, v := range curr {
                    if v == '9' {
                        digit = "0"
                    } else {
                        digit = string(v + 1)
                    }
                    nextNode := curr[:j] + digit + curr[j+1:]
                    _, okDE := deadendSet[nextNode]
                    _, ok := seen[nextNode]
                    if !okDE && !ok {
                        seen[nextNode] = true
                        dq = append(dq, nextNode)
                    }
                    if v == '0' {
                        digit = "9"
                    } else {
                        digit = string(v - 1)
                    }
                    nextNode = curr[:j] + digit + curr[j+1:]
                    _, okDE = deadendSet[nextNode]
                    _, ok = seen[nextNode]
                    if !okDE && !ok {
                        seen[nextNode] = true
                        dq = append(dq, nextNode)
                    }
                }
            }
        }
        steps++
    }
    return -1
}

func main() {
    type Pair struct {
        deadends []string
        target   string
    }
    arr := []Pair{
        {[]string{"0201", "0101", "0102", "1212", "2002"}, "0202"},
        {[]string{"8888"}, "0009"},
        {[]string{"8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"}, "8888"},
        {[]string{"0000"}, "8888"},
    }
    for _, stuff := range arr {
        fmt.Println(stuff.deadends, stuff.target)
        deadends, target := stuff.deadends, stuff.target
        r := openLock(deadends, target)
        fmt.Println(r)
    }
}

