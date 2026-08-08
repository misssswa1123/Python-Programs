class methodclass:
    college_name='DYPCOE'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def classdemo(cls,newcollege):
        cls.college_name=newcollege
    @classmethod
    def converttoformat(cls,string):
        return cls(string.split('-')[0],int(string.split('-')[1]))

# m=methodclass('Swapnali')
# print("College name=",methodclass.college_name)
# m.classdemo('DYPCOE,Akuurdi')
# print("College name=",methodclass.college_name)
# m1=methodclass('Nisha')
# m1.college_name='Hello'
# print("College name=",m1.college_name,f"Name={m1.name}")

m4=methodclass.converttoformat('swapnali-2004')
print(m4.name,m4.salary)

print(dir(m4))
print(m4.__dict__)
print(help(m4))

dict={'name':'Swapnali','Age':22}
print(dir(dict))