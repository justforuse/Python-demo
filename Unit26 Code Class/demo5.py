class FirstClass:

    def __init__(self, name, age=12):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)
x = FirstClass("allen", 21)
x.info()
