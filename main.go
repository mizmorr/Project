package main

import (
	"C"
	"Project/graphCore"
	"bufio"
	"fmt"
	"os"
	// "reflect"
	"strconv"
	"strings"
	"time"
)

//export firstSample
func firstSample(num C.int) *C.char {
	var g = graphCore.FirstSample(int(num))
	return C.CString(g)
}

//export MediumDensity
func MediumDensity(v, num C.int) *C.char {
	var g = graphCore.RandomM_Graph(int(v), int(num))
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
	reader := bufio.NewReader(os.Stdin)
	println("set parameter")
	str, _ := reader.ReadString('\n')
	num, _ := strconv.Atoi(strings.TrimSpace(str))
	t := time.Now()
	var g = (graphCore.Lastfm_Sample(num))
	dur := time.Since(t)
	defer fmt.Println("Execution time -", dur.Seconds())
	f, err := os.Create("../Документы/LastFM/last.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	_, err2 := f.WriteString(g)
	if err2 != nil {
		panic(err2)
	}
}
