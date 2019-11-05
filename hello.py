class Collegestudent:
    stream="cse"
    def __init__(self,name):
        self.name=name
    def getaddress(self,address):
        self.address=address
    def postaddress(self):
        return self.address
a=Collegestudent("karthi")
a.getaddress("kadapakkam")
print(a.postaddress())