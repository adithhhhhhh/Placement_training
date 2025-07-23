class emp:
    profit=1000000
    tax=10
    company="Cognizant"
    def __init__(self, name, sal,age,per):
        self.name = name
        self.sal = sal
        self.age = age
        self.per= per
    def cal_tax(self):
        return((emp.tax/100)*self.sal)
    def cal_share(self):
        return((self.per/100)*emp.profit)
    def display(self):
        print("Employee Name: ",self.name)
        print("Company: ",emp.company)
        print("Age: ", self.age)
        print("Salary: ",self.sal)
        print("Tax: ",self.cal_tax())
        print("Share Amount: ",self.cal_share())
        print("In hand salary: ", self.sal - self.cal_tax() + self.cal_share())
a1=emp("Adith",20000,25,4)
a2=emp("Adithya",10000,25,9)

a1.display()
print("---------------------")
a2.display()

