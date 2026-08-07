class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class marks:
    def __init__(self,total):
        self.total=total
class person(student,marks):
    def __init__(self,age,name,rollno,total):
        student.__init__(self,name,rollno)
        marks.__init__(self,total)
        self.age=age
    def display(self):
        print(f"Name= {self.name}\n rollno={self.rollno} \n total={self.total} \n age={self.age}")

p=person(22,'Swapnali',55,9.71)
p.display()
print(person.mro())

print("\n\n")

class dog: 
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Name={self.name}")
class cat:
    def __init__(self,location):
        self.location=location
    def displaycat(self):
        print(f"cat name={self.location}")
class animal(dog,cat):
    def __init__(self,name,location):
        self.name=name
        self.location=location
a=animal('Goldenretriver','Indapur')
a.display()
a.displaycat()