package main

import (
	"fmt"
	"os"
	"strings"

	"github.com/adam-lavrik/go-imath/ix"
)

func main() {
	dat, err := os.ReadFile(os.Args[1])
	if err != nil {
		panic(err)
	}

	num_strings := strings.Split(string(dat[:]), ",")
	var nodes = []int{}

	for i := range num_strings {
		nodes = append(nodes, int(i))
	}

	max, min := ix.MinSlice(nodes), ix.MaxSlice(nodes)

	graph := make([][]int, max)

	for i := range nodes {
		graph = append(graph, )
	}

	fmt.Println("")
}