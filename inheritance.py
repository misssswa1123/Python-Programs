class student:
    def __init__(self,a,b):
        self.name=a
        self.age=b
    
class score(student):
    def __init__(self,s,a,b):
        super().__init__(a,b)
        self.sc=s
    def put2(self):
        print(f"my Score is {self.sc}")
        print(f"my name is {self.name} and age is {self.age}")


# s1=student('Swapnali',22)

s2=score(2321,'Swapnali',22)

s2.put2()