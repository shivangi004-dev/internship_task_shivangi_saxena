# 5.Username Validator

def Username_Validator(user_name):
    if len(user_name) >= 5 and user_name.isalnum() and ' ' != user_name:
        return("Valid Username")
        
    else:
        return("Invalid Username")
    
print(Username_Validator("rahul123"))
print(Username_Validator("raj"))

#############################################################################################################################

# 6. Restaurant Menu Sorting
restaurant_menu=[("vadapav",50),("tea",8),("coffee",15),("pavbhaji",80),("coke",10),("dhokla",30),("samosa",12),("kachori",15)]

def sorting_by_price(item):
    return sorted(item, key=lambda x: x[1])
    
def sorting_by_name(item):
    return item[0]

def price_under_10(item):
    return item[1] <10

sorted_price = sorting_by_price(restaurant_menu)
sorted_name = sorted(restaurant_menu,key=sorting_by_name)
filtered_items = filter(price_under_10, restaurant_menu)
sorted_filtered_items = sorted(filtered_items, key=lambda item : item[0])

print("##################################")
print("Sorted by price:")
for items in sorted_price:
    print(f"{items[0]} : {items[1]}/- ")

print("##################################")
print("Sorted by name:")
for items in sorted_name:
    print(f"{items[0]} : {items[1]}/-")
    
print("##################################")
print("items priced under 10 ")
for items in sorted_filtered_items:
    print(f"{items[0]} : {items[1]}/- ")

#############################################################################################################################

# 4. Employee Management System (with Objects)
class Employee:
    employees = []
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        Employee.employees.append(self)
    
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
print("+++++++++++++++++++++++++++++++++++++")
print("Engineering Employees:")
print("+++++++++++++++++++++++++++++++++++++")
for emp in engineering_employees:
        print(emp)


total_salary_value = Employee.total_salary()
print("+++++++++++++++++++++++++++++++++++++")
print("Total Salary of All Employees:", total_salary_value)


sorted_employees = Employee.sort_by_salary()
print("+++++++++++++++++++++++++++++++++++++")
print("Employees Sorted by Salary :", sorted_employees)
print("+++++++++++++++++++++++++++++++++++++")
for emp in sorted_employees:
    print(emp)