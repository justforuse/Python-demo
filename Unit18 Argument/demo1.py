#coding=utf-8
def func(name, gender, age):
	return name, gender, age

# 按顺序
# print(func("allen", "male", 21))
# 按名称传递 关键字参数
print(func(gender="male", age=21, name="allen"))