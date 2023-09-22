class Employee:
    employee_count = 101
    def __init__(self,name,salary,designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.emp_id = "s" + str(Employee.employee_count)
        Employee.employee_count += 1
    
    def show_details(self):
        print("Employee ID : ",self.emp_id)
        print("Employee Name : ",self.name)
        print("Employee Salary : ",self.salary)
        print("Employee designation : ",self.designation)

    @classmethod
    def total_Employees(cls):
        print("Total Employees : ",cls.employee_count - 101)

emp = Employee("ganesh",1000,"IT")
emp.show_details()
emp.total_Employees()

print('')

emp = Employee("muskan",5000,"ITI")
emp.show_details()
emp.total_Employees()

print('')

emp = Employee("patel",100,"CS")
emp.show_details()
emp.total_Employees()
    
