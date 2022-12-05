package main

import (
	"C"
	"Project/graphCore"
	// "fmt"
	// "time"
)

//export firstSample
func firstSample(num int) {
	graphCore.FirstSample(num)
}

//export BigDensity
func BigDensity(v, num int) {
	graphCore.RandomBG_Graph(v, num)
}

//export Sparse
func Sparse(v, num int) {
	graphCore.RandomS_Graph(v, num)
}

//export Erdos_Renyi
func Erdos_Renyi(prob float32, v, num int) {
	graphCore.Erdos_Renyi(v, prob, num)
}

//export SecondSample
func SecondSample(num int) {
	graphCore.SecondSample(num)
}
func main() {
}
