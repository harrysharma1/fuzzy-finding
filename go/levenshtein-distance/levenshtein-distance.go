package main

import "fmt"

func min(a int,b int ,c int) int {
	if (a<=b && a<=c) {
		return a
	}else if (b<=a && b<=c){
		return b
	}else {
		return c
	}
}

func ldistance(s string, t string) int{
	m:=len(s)
	n:=len(t)
	if len(s) == 0{
		return len(t)
	}

	if len(t) == 0 {
		return len(s)
	}

	cost := 0
	if s[m-1] != t[n-1] {
		cost = 1
	}

	return min(ldistance(s[:m-1], t)+1, ldistance(s, t[:n-1])+1, ldistance(s[:m-1], t[:n-1])+cost)
}

func main()  {
	fmt.Print(ldistance("kitten","sitting"))	
	fmt.Println(ldistance("sit","git"))
}
