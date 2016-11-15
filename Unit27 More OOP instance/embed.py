class AttrDisplay:
    def gatherAttrs(self):
        attrs=[]
        for key in sorted(self.__dict__):
            attrs.append("%s=%s" % (key, getattr(self, key)))
        return ", ".join(attrs)

    def __str__(self):
        return "%s: %s" % (self.__class__.__name__, self.gatherAttrs())

class Person(AttrDisplay):

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        # int:only get the integer part
        # round: (num[, x])
        self.pay = int(self.pay * (1+percent))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, "boss", pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)

    

if __name__ == "__main__":
    bob=Manager("bob", 5000)
    print(bob)
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(sue)