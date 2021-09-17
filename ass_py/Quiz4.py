#problem 01

class Employee:
     total_employee = 0

     def __init__(self, name, work_hour):
         self.name = name
         self.work_hour = work_hour

     def __str__(self):
         s =  "Department: "+self.name+", Work hours: "+str(self.work_hour)
         return s

# Write your codes here.
class FullTimeEmployee(Employee):
    def __init__(self, name, hour):
        super().__init__(name, hour)
        print("Full time employees in Finance have to work 40 hours")
    def addFullTimeEmployee(self, *info):
        self.h =[]
        self.n = []
        self.info = info
        Employee.total_employee += len(self.info)/2
        for i in range(len(self.info)):
            if i%2 == 0:
                self.n.append(self.info[i])
            else:
                self.h.append(self.info[i])

    def __str__(self):
        x = ''
        for i in range(len(self.h)):
            x += f"\nName: {self.n[i]}, Work hours remaining: {25-self.h[i]}"

        return f"Department: {self.name}, Work hours: {self.work_hour} \nTotal Employee(s):{len(self.info)/2} \nEmployee details: {x}"
        
        

class PartTimeEmployee(Employee):
    def __init__(self, name, hour):
        super().__init__(name, hour)
        print("Part time employees of Other Section have to work 25 hours.")
    def addPartTimeEmployee(self, *info):
        self.h =[]
        self.n = []
        self.info = info
        Employee.total_employee += len(self.info)/2
        for i in range(len(self.info)):
            if i%2 == 0:
                self.n.append(self.info[i])
            else:
                self.h.append(self.info[i])

    def __str__(self):
        x = ''
        for i in range(len(self.h)):
            x += f"\nName: {self.n[i]}, Work hours remaining: {25-self.h[i]}"

        return f"Department: {self.name}, Work hours: {self.work_hour} \nTotal Employee(s):{len(self.info)/2} \nEmployee details: {x}"
        


# Do not change the following lines of code.
p1 = FullTimeEmployee("Finance", 40 )
print("=================================")
p1.addFullTimeEmployee("Bob", 12,  "Carol", 18, "Mike", 15)
print("=================================")
print(p1)
print("=================================")
p2 = PartTimeEmployee("Others", 25)
print("=================================")
p2.addPartTimeEmployee("David", 12, "Simon", 18)
print("=================================")
print(p2)
print("=================================")
print("Total Employee ", Employee.total_employee)   