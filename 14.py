class Company:
    def __init__(self, CompanyName, city, mobile_no):
        self.CompanyName = CompanyName
        self.city = city
        self.mobile_no = mobile_no
    
class Employee(Company):
    def __init__(self, CompanyName, city, mobile_no, emp_name, designation, salary):
        # Call the constructor of the parent class
        super().__init__(CompanyName, city, mobile_no)
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary
    
employee1 = Employee("Techrover Solutions", "Gujarat", "123-456-7890", "Maya Malhotra", "Project Manager", 85000)

#print(employee1.CompanyName, employee1.city, employee1.mobile_no,  employee1.emp_name, employee1.designation, employee1.salary) 

print(employee1.CompanyName)
print(employee1.city)
print(employee1.mobile_no)
print(employee1.emp_name)
print(employee1.designation)
print(employee1.salary)
