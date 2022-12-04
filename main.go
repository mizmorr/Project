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

}
