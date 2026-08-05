class student:
    def __init__(self,n,a):
        print("Hello from constructor") #it runs even after the only creating instance of the class
        self.name=n
        self.age=a
    # def getdata(self):
    #     self.name=input("Enter Name=")
    #     self.age=int(input("Enter age="))

    def putdata(self):
        print(f"My name is {self.name} and age is {self.age}")

    def __del__(self):
        print("object deleted!!!")

s1=student('Swapnali',22)
s1.putdata()
del s1
s1.putdata()#gives the error ad onject s1 not defined

# s1.getdata()
# s1.putdata()

# s2=student()
# s2.getdata()
# s2.putdata()
# print(s2)
