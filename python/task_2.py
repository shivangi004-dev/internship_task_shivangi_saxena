   # 4. Employee Management System (with Objects)
class Employee:
    employees = []
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        Employee.employees.append(self)
        
    def details(self):
        return(f"emp_id: {self.emp_id}\nname: {self.name}\ndepartment: {self.department}\nsalary: {self.salary}")
    def __str__(self):
        return f"emp_id: {self.emp_id}, name: {self.name}, department: {self.department}, salary: {self.salary}"
    
    def find_engineering_employees():
        return [emp for emp in Employee.employees if emp.department == "Engineering"]
        
    def total_salary():
        return sum(emp.salary for emp in Employee.employees)
        
    def sort_by_salary():
        return sorted(Employee.employees, key=lambda emp: emp.salary, reverse=True)
    
    def add_employee(emp_id, name, department, salary):
        return Employee(emp_id, name, department, salary)
    
Employee.add_employee(1, "rahul singh", "Engineering", 50000)
Employee.add_employee(2, "harsh jain", "Marketing", 45000)
Employee.add_employee(3, "aditi jain", "Engineering", 70000)
Employee.add_employee(4, "sunita sharma", "Sales", 55000)

engineering_employees = Employee.find_engineering_employees()
print("Engineering Employees:")
for emp in engineering_employees:
        print(emp)
total_salary_value = Employee.total_salary()
print("Total Salary of All Employees:", total_salary_value)

sorted_employees = Employee.sort_by_salary()
print("Employees Sorted by Salary :", sorted_employees)
for emp in sorted_employees:
    print(emp)