class student:
    def __init__(self):
        self._name="Swapnali"
        self.__rollno=55
    def _function(self):
        print(self._name)
        print(self.__rollno)
class demo(student):
    pass
d=demo()
s=student()
d._function()
print(d._name)# act like protected accessed by the subclass and the class itself.
print(s._student__rollno)#act like private only accessed by the class where it resides

# Static Method 

class demo:
    def __init__(self,num):
        self.num=num
    def display(self,n):
        return self.num+n
    @staticmethod
    def add(a,b):
        return a+b

d=demo(2)
print(d.display(4))
print(demo.add(1,2))

