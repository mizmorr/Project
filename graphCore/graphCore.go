package graphCore

import (
	"bufio"
	"fmt"
	"io"
	"io/ioutil"
	"math/rand"
	"sort"
	"strconv"
	"strings"
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
func Erdos_Renyi(g graph, prob float32) {
	for j := range g.adj {
		for k := range g.adj {
			p := rand.Float32()
			if k != j && p <= prob == true {
				g.addEdge(k, j)
			}
		}
	}
}
func GraphCreateV(V int) (g graph) {
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

func Different_Mark(list []int) (g graph, m_v map[int]int) {
	g = GraphCreateV(len(list))
	m_v = make(map[int]int)
	for i := range list {
		m_v[i] = list[i]
	}
	return
}
func FirstSample() (g1 graph) {
	g1 = GraphCreateV(9)
	g1.addEdge(0, 1)
	g1.addEdge(0, 2)
	g1.addEdge(0, 3)
	g1.addEdge(0, 4)
	g1.addEdge(0, 5)
	g1.addEdge(1, 2)
	g1.addEdge(1, 3)
	g1.addEdge(1, 4)
	g1.addEdge(1, 5)
	g1.addEdge(2, 3)
	g1.addEdge(2, 4)
	g1.addEdge(2, 5)
	g1.addEdge(2, 6)
	g1.addEdge(3, 6)
	g1.addEdge(3, 7)
	g1.addEdge(3, 4)
	g1.addEdge(4, 8)
	g1.addEdge(5, 6)
	g1.addEdge(6, 7)
	g1.addEdge(7, 8)
	g1.k_coreLabel()
	return
}

func (g graph) Particular_K_Core(k int) {
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
		fmt.Println("no such k-core found")
	} else {
		fmt.Println(k, " - core:")
		for _, i := range w {
			fmt.Print(i, " ")
		}
		fmt.Println()
	}
}

func (g graph) MaxKCore() {
	var max int = g.coreNumber[0]
	for _, i := range g.coreNumber {
		if i > max {
			max = i
		}
	}
	fmt.Println(max)
}
func (g graph) TestMaxCore() {
	t := make([]int, len(g.coreNumber))
	copy(t, g.coreNumber)
	sort.Ints(t)
	var max = t[len(t)-1]
	fmt.Print(max)
}

func (g graph) Particular_K_CoreM(k int, m_v map[int]int) {
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
		fmt.Println("no such k-core found")
	} else {
		fmt.Println(k, " - core:")
		for _, i := range w {
			fmt.Print(m_v[i], " ")
		}
		fmt.Println()
	}
}

func (g graph) MaxKCoreM(m_v map[int]int) {
	var max int = g.coreNumber[0]
	for _, i := range g.coreNumber {
		if i > max {
			max = i
		}
	}
	g.Particular_K_CoreM(max, m_v)
}

func (g graph) All_K_Cores() {
	klist := g.coreNumber
	k2 := make(map[int]int)
	for i := range klist {
		if _, ok := k2[klist[i]]; !ok {
			k2[klist[i]] = 0
			g.Particular_K_Core(klist[i])
		}
	}
}

func (g graph) All_K_CoresM(m_v map[int]int) {
	klist := g.coreNumber
	k2 := make(map[int]int)
	for i := range klist {
		if _, ok := k2[klist[i]]; !ok {
			k2[klist[i]] = 0
			g.Particular_K_CoreM(klist[i], m_v)
		}
	}
}

func makeGtxt(txt []int, V int) graph {
	g := GraphCreateV(V)
	for i := 0; i < len(txt)-1; i += 2 {
		g.addEdge(txt[i], txt[i+1])
	}
	return g
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
