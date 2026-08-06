class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print(f"The name is {self.name} and age is {self.age}")
class student(person):
    def __init__(self,rollno,course,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.course=course
    def display_student(self):
        print(f"roll no is {self.rollno} and course is {self.course}")
class garduate_student(student):
    def __init__(self,research_topic,guide,rollno,course,name,age):
        super().__init__(rollno,course,name,age)
        self.research_topic=research_topic
        self.guide=guide
    def display_research(self):
        print(f"Research Topic={self.research_topic} and guide= {self.guide}")

g=garduate_student('ML types','Ms.Anagha Darokar',55,'CSE','Swapnali',22)
g.display_person()
g.display_student()
g.display_research()
print("\n Name is",g.name)
print("\n rollno:",g.rollno)

        
