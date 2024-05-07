import sys

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, age1, age2):
        deleted = False
        for emp in self.employees[:]:
            if emp.age in range(age1, age2+1):
                print(f"Deleting {emp.name} (age {emp.age})")
                self.employees.remove(emp)
                deleted = True
        if not deleted:
            print("There are no employees in this age range.")

    def update_salary(self, name, new_salary):
        for emp in self.employees:
            if emp.name == name:
                emp.salary = new_salary
                break
        else:
            print("No employee with such a name.")

    def display(self):
        if not self.employees:
            print("There are no employees.")
            return
        print("Employees list:")
        for emp in self.employees:
            print(f"{emp.name} (age {emp.age}) - Salary: {emp.salary}")

class FrontEndManager(EmployeesManager):
    manager = EmployeesManager()
    while True:
        try:
            x = int(input('''Program Options:
1) Add a new employee
2) List all employees
3) Delete by age range
4) Update salary given a name
5) End the program
Enter your choice (from 1 to 5): '''))
        except ValueError:
            print("Invalid input, please enter an integer.")
            continue
        if x not in range(1, 6):
            print("Invalid input, please enter a number between 1 and 5.")
            continue
        if x == 1:
            name = input("Enter the name of the employee: ")
            try:
                age = int(input("Enter the age of the employee: "))
                salary = int(input("Enter the salary of the employee: "))
                emp = Employee(name, age, salary)
                manager.add_employee(emp)
            except ValueError:
                print("Invalid input, please enter an integer.")
        elif x == 2:
            manager.display()
        elif x == 3:
            try:
                age1 = int(input("Enter age from: "))
                age2 = int(input("Enter age to: "))
                manager.remove_employee(age1, age2)
            except ValueError:
                print("Invalid input, please enter an integer.")
        elif x == 4:
            name = input("Enter the name: ")
            try:
                new_salary = int(input("Enter the new salary: "))
                manager.update_salary(name, new_salary)
            except ValueError:
                print("Invalid input, please enter an integer.")
        elif x == 5:
            sys.exit()
