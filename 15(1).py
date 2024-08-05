# Base class 1
class Company:
    def __init__(self, CompanyName, city, mobile_no):
        self.CompanyName = CompanyName
        self.city = city
        self.mobile_no = mobile_no

# Base class 2
class Person:
    def __init__(self, emp_name, age):
        self.emp_name = emp_name
        self.age = age

# Derived class
class Employee(Company, Person):
    def __init__(self, CompanyName, city, mobile_no, emp_name, age, designation, salary):
        # Call the constructors of both parent classes
        Company.__init__(self, CompanyName, city, mobile_no)
        Person.__init__(self, emp_name, age)
        self.designation = designation
        self.salary = salary

    def display_details(self):
        print(employee1.CompanyName)
        print(employee1.city)
        print(employee1.mobile_no)
        print(employee1.emp_name)
        print(employee1.designation)
        print(employee1.salary)

# Creating an object of the Employee class
employee1 = Employee("Techrover Solutions", "Gujarat", "123-456-7890", "Maya Malhotra", 35, "Project Manager", 85000)

# Displaying the employee's full details
employee1.display_details()
