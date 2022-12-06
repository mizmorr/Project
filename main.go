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
	start := time.Now()
	var g = graphCore.RandomBG_Graph(int(v), int(num))
	duration := time.Since(start)
	dur := fmt.Sprintln(duration.Seconds())
	res := dur + g
	return C.CString(res)
}

//export Sparse
func Sparse(v, num C.int) *C.char {
	start := time.Now()
	var g = graphCore.RandomS_Graph(int(v), int(num))
	duration := time.Since(start)
	dur := fmt.Sprintln(duration.Seconds())
	res := dur + g
	return C.CString(res)
}

//export Erdos_Renyi
func Erdos_Renyi(prob C.float, v, num C.int) *C.char {
	start := time.Now()
	var g = graphCore.Erdos_Renyi(int(v), float32(prob), int(num))
	duration := time.Since(start)
	dur := fmt.Sprintln(duration.Seconds())
	res := dur + g
	return C.CString(res)
}

//export Last_Sample
func Last_Sample(num C.int) *C.char {

	start := time.Now()
	var g = graphCore.Lastfm_Sample(int(num))
	duration := time.Since(start)
	dur := fmt.Sprintln(duration.Seconds())
	res := dur + g
	return C.CString(res)
}

//export SecondSample
func SecondSample(num C.int) *C.char {
	start := time.Now()
	var g = graphCore.SecondSample(int(num))
	duration := time.Since(start)
	dur := fmt.Sprintln(duration.Seconds())
	res := dur + g
	return C.CString(res)
}

func main() {
}
