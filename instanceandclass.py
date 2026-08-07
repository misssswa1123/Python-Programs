class student:
    college="DYPCOE"
    total_stu=0
    def __init__(self,name):
        self.name=name
        student.total_stu+=1
    def display(self):
        print(f"Name={self.name} and college={self.college} and total_stu={self.total_stu}")

s1=student("Swapnali")
s1.display()
student.college="DYPCOE,Akurdi"
s2=student("Nisha")
s2.display()
s3=student("Arshad")
s3.display()
