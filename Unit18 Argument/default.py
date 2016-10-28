# coding=utf-8
# name=value形式在调用和def中有不同的含义
# 调用时代表关键字参数，def中代表默认值参数

def func(a,b=2,c=3):
	print(a,b,c)

func(1)
func(a=1)
func(5,6,7)
func(5,6)

func(5, c="c")