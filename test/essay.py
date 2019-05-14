#!/usr/bin/env python3
#coding=utf-8

import numpy

def sfft(data):
	result = numpy.fft.fft(data)
	#real = result.real
	#imag = result.imag
	return result

