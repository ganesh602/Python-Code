class Student:
    def __init__(self,roll,name,department):
        self.roll = roll
        self.name = name
        self.department = department

    def display(self):
        #print("Roll No :",self.roll,"\nName :",self.name,"\nDepartment :",self.department)
        print(f"Roll No : {self.roll} \nName : {self.name} \nDepartment : {self.department}")