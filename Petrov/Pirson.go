package main

import (
	"math"
)

type Pirson struct {
	count map[int32]int32
	l     int32
	y     map[int32]float64
}

type PirsonAgrs<T> struct {
	x
}

func NewPirson(args PirsonAgrs) {

}

func (this Pirson) get_stat() float64 {
	n := this.count
	l := float64(this.l)
	p := this.y

	var X float64
	for i, pi := range p {
		X += math.Pow(float64(float64(n[i])-l*pi), 2.0) / (l * pi)
	}
	return X
}

func (this *Pirson) counter(arr []int32) map[int32]int32 {
	out := make(map[int32]int32, len(arr))
	for i := range arr {
		out[int32(i)]++
	}
	return out
}

func (this *Pirson) transform_range_to_array() {

}
