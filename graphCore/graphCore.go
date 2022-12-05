package graphCore

import (
	"bufio"
	"fmt"
	"io"
	"io/ioutil"
	"math/rand"
	"strconv"
	"strings"
	"time"
)

type graph struct {
	adj        [][]int
	coreNumber []int
}

func contains(r []int, e int) bool {
	for _, j := range r {
		if j == e {
			return true
		}
	}
	return false
}

func (g graph) addEdge(vertex_fst int, vertex_snd int) {
	if !contains(g.adj[vertex_fst], vertex_snd) && vertex_fst != vertex_snd {
		g.adj[vertex_fst] = append(g.adj[vertex_fst], vertex_snd)
		g.adj[vertex_snd] = append(g.adj[vertex_snd], vertex_fst)
	}
}

func (g graph) graphLabel() (res []int) {
	res = make([]int, len(g.adj))
	for i := 0; i < len(g.adj); i++ {
		res[i] = len(g.adj[i])
	}
	return
}

func makeRange(min, max int) []int {
	a := make([]int, max-min+1)
	for i := range a {
		a[i] = min + i
	}
	return a
}

func Erdos_Renyi(v int, prob float32, num int) string {
	g := graphCreateV(v)
	for j := range g.adj {
		for k := range g.adj {
			p := rand.Float32()
			if k != j && p <= prob == true {
				g.addEdge(k, j)
			}
		}
	}
	switch num {
	case 0:
		return g.all_K_Cores()
	case 1:
		return g.maxKCore()
	default:
		return g.particular_K_Core(num)
	}
}

func graphCreateV(V int) (g graph) {
	vert_list := make([][]int, V)
	i := 0
	for i < V {
		vert_list[i] = make([]int, 0)
		i++
	}
	coreNums := make([]int, V)
	g = graph{vert_list, coreNums}
	return
}

func graphCreate_DM(list []string) (g graph, m_v map[int]string) {
	g = graphCreateV(len(list))
	m_v = make(map[int]string)
	for i := range list {
		m_v[i] = list[i]
	}
	return
}

func remove(a []int, key int) (r []int) {
	set := make(map[int]int)
	for i := range a {
		set[a[i]] = i
	}
	delete(set, key)
	r = make([]int, 0)
	for k := range set {
		r = append(r, k)
	}

	return
}
func SecondSample(num int) string {
	premark := getMark("graphCore/second_sample_marks.txt")
	g, mark := graphCreate_DM(premark)
	g.k_coreLabel()
	switch num {
	case 0:
		return g.all_K_CoresM(mark)
	case 1:
		return g.maxKCoreM(mark)
	default:
		return g.particular_K_CoreM(num, mark)
	}

}
func removeArray(a [][]int, key int) (ar [][]int) {
	set := make(map[int][]int)
	for j := range a {
		if j != key {
			set[j] = remove(a[j], key)
		} else {
			set[j] = make([]int, 0)
		}
	}
	ar = make([][]int, len(a))
	for l := range set {
		ar[l] = set[l]
	}
	return
}

func (g graph) k_coreLabel() {
	var k int = 0
	V := makeRange(0, len(g.adj)-1)
	d := g.graphLabel()
	for len(V) > 0 {
		k++
		unpocessedV := V
		for len(unpocessedV) > 0 {
			v := unpocessedV[0]
			unpocessedV = unpocessedV[1:]
			if d[v] < k {
				for _, w := range g.adj[v] {
					d[w]--
					unpocessedV = append(unpocessedV, w)
				}
				g.coreNumber[v] = k - 1
				V = remove(V, v)
				g.adj = removeArray(g.adj, v)
			}
		}
	}
}

func (g graph) particular_K_CoreM(k int, m_v map[int]string) (res string) {
	w := func() []int {
		ar := []int{}
		for i := range g.coreNumber {
			if g.coreNumber[i] == k {
				ar = append(ar, i)
			}
		}
		return ar
	}()
	if len(w) == 0 {
		res += fmt.Sprintln("no such k-core found")
	} else {
		res += fmt.Sprintln(k, " - core:")
		for _, i := range w {
			res += fmt.Sprint(m_v[i], " ")
		}
		res += fmt.Sprintln()
	}
	return
}
func makeRandEdges(g graph) {
	for j := range g.adj {
		k := rand.Intn(len(g.adj))
		prob := rand.Intn(2)
		if prob != 0 {
			g.addEdge(j, k)
		}
	}
}
func randG_almostSparse(V int) graph {
	g := graphCreateV(V)
	go makeRandEdges(g)
	go makeRandEdges(g)
	time.Sleep(time.Millisecond * 1)
	return g
}

func randG_bigDensity(V int) graph {
	g := graphCreateV(V)
	go makeRandEdges(g)
	go makeRandEdges(g)
	go makeRandEdges(g)
	go makeRandEdges(g)
	go makeRandEdges(g)
	go makeRandEdges(g)
	time.Sleep(time.Millisecond * 1)
	return g
}

func (g graph) maxKCoreM(m_v map[int]string) string {
	var max int = g.coreNumber[0]
	for _, i := range g.coreNumber {
		if i > max {
			max = i
		}
	}
	return g.particular_K_CoreM(max, m_v)
}

func (g graph) maxKCore() string {
	var max int = g.coreNumber[0]
	for _, i := range g.coreNumber {
		if i > max {
			max = i
		}
	}
	return g.particular_K_Core(max)
}

func Lastfm_Sample(num int) string {
	g := graphCreateV(7624)
	edges := getEdges("graphCore/lastfm_asia_edges.txt")
	makeGDM(g, edges)
	g.k_coreLabel()
	switch num {
	case 0:
		return g.all_K_Cores()
	case 1:
		return g.maxKCore()
	default:
		return g.particular_K_Core(num)
	}
}

func (g graph) all_K_Cores() (res string) {
	klist := g.coreNumber
	k2 := make(map[int]int)
	for i := range klist {
		if _, ok := k2[klist[i]]; !ok {
			k2[klist[i]] = 0
			res += fmt.Sprintln(g.particular_K_Core(klist[i]))
		}
	}
	return
}

func (g graph) all_K_CoresM(m_v map[int]string) (res string) {
	klist := g.coreNumber
	k2 := make(map[int]int)
	for i := range klist {
		if _, ok := k2[klist[i]]; !ok {
			k2[klist[i]] = 0
			res += fmt.Sprintln(g.particular_K_CoreM(klist[i], m_v))
		}
	}
	return
}

func getMark(s string) []string {
	var result []string
	f, err := ioutil.ReadFile(s)
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(strings.NewReader(string(f)))
	scanner.Split(bufio.ScanWords)
	for scanner.Scan() {
		s := strings.Split(scanner.Text(), ",")
		result = append(result, s[1])
	}
	return result
}
func getEdges(s string) []int {
	var result []int
	f, err := ioutil.ReadFile(s)
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(strings.NewReader(string(f)))
	scanner.Split(bufio.ScanWords)
	for scanner.Scan() {
		s := strings.Split(scanner.Text(), ",")
		for _, j := range s {
			postj, err := strconv.Atoi(j)
			if err != nil {
				panic(err)
			}
			result = append(result, postj)
		}
	}
	return result
}
func printG(g graph) {
	for _, j := range g.adj {
		fmt.Println(j)
	}
}
func FirstSample(num int) string {
	g := MakeG_txt("graphCore/first_sample.txt", 9)
	g.k_coreLabel()
	switch num {
	case 0:
		return g.all_K_Cores()
	case 1:
		return g.maxKCore()
	default:
		return g.particular_K_Core(num)
	}

}
func RandomBG_Graph(v int, num int) string {
	g := randG_bigDensity(v)
	g.k_coreLabel()
	switch num {
	case 0:
		return g.all_K_Cores()
	case 1:
		return g.maxKCore()
	default:
		return g.particular_K_Core(num)
	}

}
func RandomS_Graph(v int, num int) string {
	g := randG_almostSparse(v)
	g.k_coreLabel()
	switch num {
	case 0:
		return g.all_K_Cores()
	case 1:
		return g.maxKCore()
	default:
		return g.particular_K_Core(num)
	}
}

func GitSample() (graph, map[int]string) {
	premark := getMark("graphCore/git_marks.txt")
	g, mark := graphCreate_DM(premark)
	edges := getEdges("graphCore/git_edges.txt")
	makeGDM(g, edges)
	return g, mark
}

func (g graph) particular_K_Core(k int) (res string) {
	w := func() []int {
		ar := []int{}
		for i := range g.coreNumber {
			if g.coreNumber[i] == k {
				ar = append(ar, i)
			}
		}
		return ar
	}()
	if len(w) == 0 {
		res += fmt.Sprintln("no such k-core found")
	} else {
		res += fmt.Sprintln(k, " - core:")
		for _, i := range w {
			res += fmt.Sprint(i, " ")
		}
	}
	return
}

func makeGtxt(txt []int, V int) graph {
	g := graphCreateV(V)
	for i := 0; i < len(txt)-1; i += 2 {
		g.addEdge(txt[i], txt[i+1])
	}
	return g
}
func makeGDM(g graph, txt []int) {
	for i := 0; i < len(txt)-1; i += 2 {
		g.addEdge(txt[i], txt[i+1])
	}

}
func makeInt_frm_txt(r io.Reader) ([]int, error) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanWords)
	var result []int
	for scanner.Scan() {
		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return result, err
		}
		result = append(result, x)
	}
	return result, scanner.Err()
}
func MakeG_txt(s string, V int) graph {

	f, err := ioutil.ReadFile(s)
	if err != nil {
		panic(err)
	}
	cont, err2 := makeInt_frm_txt(strings.NewReader(string(f)))
	if err2 != nil {
		panic(err2)
	}
	return makeGtxt(cont, V)
}
