# 1. Weather Data Analysis
temperatures = [32, 35, 28, 30, 33, 31, 29]
below_30_count = 0
temperatures_in_fahrenheit = []

hottest_temp=max(temperatures)
coldest_temp=min(temperatures)
print(f"hottest tempertaute:{hottest_temp}\ncoldest temperature:{coldest_temp}")

for temp in temperatures:
    if temp < 30:
        below_30_count += 1
print(f"Number of days below 30°C: {below_30_count}")


for temp in temperatures:
    temp_into_fahrenheit=temp*1.8+32
    temperatures_in_fahrenheit.append(temp_into_fahrenheit)
print(f"Temperatures in Fahrenheit: {temperatures_in_fahrenheit}")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#2. Grocery Store Inventory
inventory = [
    {"name": "Milk", "quantity": 10, "price": 2.5},
    {"name": "Eggs", "quantity": 30, "price": 0.2},
    {"name": "Bread", "quantity": 15, "price": 1.5},
    {"name": "Butter", "quantity": 5, "price": 3.0},
]
total_value=sum(item["quantity"]*item["price"] for item in inventory)
print(f"Total values in the inventory : {total_value}")

inventory.append({"name": "Cheese", "quantity": 20, "price": 2.0 })
print(f"updated_inventory:{inventory}")

lowest_quantity_item=min(inventory, key= lambda item: item["quantity"])
print(f"lowest quantity item:{lowest_quantity_item}")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#3. School Student Records
students = [
    {"name": "Alice", "age": 14, "grades": [85, 90, 78]},
    {"name": "Bob", "age": 15, "grades": [88, 74, 92]},
    {"name": "Charlie", "age": 14, "grades": [95, 80, 85]},
]

for stud in students:
    avg_grade_of_students=sum(stud["grades"])/len(stud["grades"])
    stud["average_garde"]=avg_grade_of_students
print(f"updated list:{students}")

highest_avg_grade=max(students,key=lambda stud:stud["average_garde"])
print(f"highest average grade:{highest_avg_grade["name"]}")

students.append({"name":"sonia","age":23,"grades":[89,98,87],"average_garde":91.33})
print(students)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#4. Employee Directory

employees = [
    {"name": "John", "role": "Manager", "salary": 5000},
    {"name": "Jane", "role": "Developer", "salary": 4000},
    {"name": "Sam", "role": "Designer", "salary": 3500},
    {"name": "Anna", "role": "Developer", "salary": 4000},
]
def find_developers(employees):
    developers = [employee for employee in employees if employee["role"] == "Developer"]
    return developers
def calculate_total_salary(employees):
    total_salary = sum(employee["salary"] for employee in employees)
    return total_salary

developers = find_developers(employees)
print("Employees with the role 'Developer':")
for dev in developers:
    print(dev["name"])

total_salary = calculate_total_salary(employees)
print(f"Total salary paid by the company:{total_salary}")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#5. Flight Booking System
passengers = [
 {"name": "Alice", "flight": "A123", "seat": "12A", "checkedIn": True},
 {"name": "Bob", "flight": "A123", "seat": "14B", "checkedIn": False},
 {"name": "Charlie", "flight": "B456", "seat": "22C", "checkedIn": True},
 ]

def count_checked_in_A123(passengers):
    count=0
    for passenger in passengers:
        if passenger["flight"] == "A123" and passenger["checkedIn"]:
            count+= 1
    return count
def find_passengers_on_B456(passengers):
    b456_passengers = [passenger["name"] for passenger in passengers if passenger["flight"] == "B456"]
    return b456_passengers
def update_seat_for_bob(passengers):
    for passenger in passengers:
        if passenger["name"] == "Bob":
            passenger["seat"] = "15C"
    return

checked_in=count_checked_in_A123(passengers)
print(f"no. of checked in in A123:{checked_in}")

b456_passengers = find_passengers_on_B456(passengers)
print(f"Passengers on flight B456: {b456_passengers}")

update_seat_for_bob(passengers)
print(passengers)