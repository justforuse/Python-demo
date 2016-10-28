def reg(name, age, **kw):
    print({"name": name, "age": age, "other": kw})

reg("allen", 21)
reg("bob", 18, city="beijing")
