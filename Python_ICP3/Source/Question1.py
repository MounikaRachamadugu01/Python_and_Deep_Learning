""" Create a class Employee and then do the following:
Create a data member to count the number of Employees
Create a constructor to initialize name, family, salary, department
Create a function to average salary
Create a Full time Employee class and it should inherit the properties of Employee class
Create the instances of Full time Employee class and Employee class and call their member functions."""

# create Employee class
class Employee:
    noOfEmployees = 0
    empSalary = 0

    # Define a constructor method
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.noOfEmployees += 1
        Employee.empSalary = Employee.empSalary+self.salary

    # This method returns average salary of the Employees
    def averageSalary(self):
        avgSalary = Employee.empSalary/Employee.noOfEmployees
        return(print("Average Salary of the Employees:", avgSalary))

    # This method prints the Employee Details
    def displayEmpDetails(self):
        print("\n Employee Name:",self.name, "\n Family:", self.family, "\n Salary:", self.salary, "\n Department:", self.department, "\n")

# create Fulltime Employee Class
class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


a = Employee('Mounika', 'Rachamadugu', 150000, 'CSE')
b = Employee('Mouni', 'Menneni', 250000, 'ECE')
c = FulltimeEmployee('Monica', 'RM', 200000, 'EEE')

a.displayEmpDetails()
b.displayEmpDetails()
c.displayEmpDetails()

# Display total number of employees
print("Total No. of Employees:", Employee.noOfEmployees)
# Calling Average Salary method of Employee Class
a.averageSalary()

