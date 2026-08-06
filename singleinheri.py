class animal:
    def __init__(self,name,location):
        self.name=name
        self.location=location
class type(animal):
    def __init__(self,name,location,breed):
        # animal.__init__(self,name,location)
        super().__init__(name,location)
        self.breed=breed
    def display(self):
        print(f"Name= {self.name} location={self.location}")
        print("Breed",self.breed)
t=type('dog','pune','Golden retriver')
t.display()
print("\n\n")
class hospital_staff:
    def __init__(self,staff_id,name,work_shift):
        self.staff_id=staff_id
        self.name=name
        self.work_shift=work_shift
    def display_details(self):
        print(f"Staff_id:\t{self.staff_id}\nName:\t{self.name}\nWork_shift:\t{self.work_shift}")
class doctor(hospital_staff):
    def __init__(self,specialization,patients_treated,staff_id,name,work_shift):
        super().__init__(staff_id,name,work_shift)
        self.specialization=specialization
        self.patients_treated=patients_treated
    def diagnose(self):
        print("Specialization of doctor=\t",self.specialization)
        print("Patients_Treated=\t",self.patients_treated)
        print("\n Patient has beed diagnosed with the Diarrehea")
    def prescibe_medicine(self):
        print("\n ******Prescription*********")
        print("Drink ORS or Coconut water")
        print("Dont eat spicy")
        print("Eat O2 and other medicnes written!!")
d=doctor("Homopathy",23,102,'dr.Nisha Chavan',"10 am ti 5 pm")
d.display_details()
d.diagnose()
d.prescibe_medicine()

print("Name of doctor=",d.name)
print("\n\n")
class demo:
    name="Swapnali"
    age=22
class demo1(demo):
    grade="BE"
    def display(self):
        print(self.name)
        print(self.age)
        print(self.grade)
d=demo1()
d.display()
print(d.name)
print(d.age)
print(d.grade)