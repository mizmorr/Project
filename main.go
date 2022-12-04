package main

import (
	"C"
	"Project/graphCore"
	"fmt"
	"time"
)

//export firstSample
func firstSample() {
	g := graphCore.FirstSample()
	g.All_K_Cores()
}
func main() {
	// start := time.Now()
	// graphCore.GitSample()
	// duration := time.Since(start)

	// fmt.Println(dur.Seconds(), duration.Seconds())
	g := graphCore.RandG_almostSparse(4000)
	st := time.Now()
	graphCore.Atest(g)
	dur := time.Since(st)
	fmt.Println(dur.Seconds())

	start1 := time.Now()
	g.MaxCore()
	duration1 := time.Since(start1)
	start2 := time.Now()
	g.TMaxKCore()
	duration2 := time.Since(start2)
	fmt.Println(duration1.Seconds(), duration2.Seconds())

}
