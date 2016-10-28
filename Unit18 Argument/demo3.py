# coding=utf-8
def func(a, *args, **targs):
    print(a, args, targs)

# 不能再定义一个a=1
func(1, 2, 3, 4, b=1, c=2)
