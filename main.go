package main

import (
	"C"
	"Project/graphCore"
	"fmt"
	// "reflect"
	// "strconv"
	"time"
)

//export firstSample
func firstSample(num C.int) *C.char {
	start := time.Now()
	var g = graphCore.FirstSample(int(num))
	duration := time.Since(start)
	dur := fmt.Sprintln(duration.Seconds())
	res := dur + g
	return C.CString(res)
}

//export BigDensity
func BigDensity(v, num C.int) *C.char {
	var g = graphCore.RandomBG_Graph(int(v), int(num))
	return C.CString(g)
}

//export Sparse
func Sparse(v, num C.int) *C.char {
	var g = graphCore.RandomS_Graph(int(v), int(num))
	return C.CString(g)
}

//export Erdos_Renyi
func Erdos_Renyi(prob C.float, v, num C.int) *C.char {
	var g = graphCore.Erdos_Renyi(int(v), float32(prob), int(num))
	return C.CString(g)
}

//export Last_Sample
func Last_Sample(num C.int) *C.char {
	var g = graphCore.Lastfm_Sample(int(num))
	return C.CString(g)
}

//export SecondSample
func SecondSample(num C.int) *C.char {
	var g = graphCore.SecondSample(int(num))
	return C.CString(g)
}
func main() {
}
