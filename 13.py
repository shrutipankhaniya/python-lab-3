class employee:
    def __init__(self, name, DateOfJoin, designation, Salary):
        self.name = name
        self.DateOfJoin = DateOfJoin
        self.designation = designation
        self.Salary = Salary
p1 = employee("Maya", "19/6/2024", "Manager", 30000)
print(p1.name, p1.DateOfJoin, p1.designation, p1.Salary)

print(p1.DateOfJoin)
print(p1.designation)
print(p1.Salary)
