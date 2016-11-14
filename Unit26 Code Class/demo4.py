class A(object):
    def __init__(self, name):
        self.name=name
        print ("name:", self.name)
    def getName(self):
        return 'A ' + self.name

class B(A):
    def __init__(self, name):
        super(B, self).__init__(name)
        print ("hi")
    def getName(self):
        return 'B '+self.name

if __name__=='__main__':
    b=B('hello')
    print (b.getName())