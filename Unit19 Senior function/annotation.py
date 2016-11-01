def func(a: "userName", b: "userAge"=18) -> "userInfo":
    print(a, b)

func("allen")
print(func.__annotations__)