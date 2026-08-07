class A:
    def demo(self):
        print("Class A")
class B(A):
    def demoB(self):
        print("Class B")
class C(A):
    def demoC(self):
        print("Class C")
c=C()
a=B()
c.demo()
c.demoC()
a.demo()
a.demoB()


class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display_student(self):
        print(f"Name of student={self.name}\n roll no: {self.rollno}")
class engineeringstudent(student):
    def __init__(self,branch,name,rollno):
        super().__init__(name,rollno)
        self.branch=branch
    def display(self):
        super().display_student()
        print("Branch of Student=",self.branch)
class extrawork(engineeringstudent):
    def __init__(self,extra,branch,name,rollno):
        super().__init__(branch,name,rollno)
        self.extra=extra
    def displayextra(self):
        super().display()
        print("Extra tasks",self.extra)
e=extrawork('CRPC volunteer','CSE','Swapnali',55)
e.displayextra()
print(extrawork.mro())
e.display_student()

