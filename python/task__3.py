# 7. Exam Grading System
from functools import reduce
scores=[85,92,78,88,76,95]

result_1=all(s >= 50 for s in scores)
print("students scored atleast 50:",result_1)

result_2=any(s > 90 for s in scores)
print("students scored above 90:",result_2)

result_3= reduce(lambda x,y: x+y, scores)
average_score=result_3/6
print("average score of the students:",average_score)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 8. Employee Salary Updates

employees = [
    {"name": "Alice", "salary": 4000},
    {"name": "Bob", "salary": 3000},
    {"name": "Charlie", "salary": 5000},
    {"name": "Dave", "salary": 2500},
]

raised_salary=list(map(lambda emp:{"name":emp["name"],"salary":emp["salary"]*10},employees))
print("employee with 10% raise:" ,raised_salary)

total_salary=reduce(lambda acc,emp : acc+emp['salary'],employees,0)
print("total salary:", total_salary)

salary_above_4000=next((emp for emp in employees if emp['salary']>4000),None)
print("First Employee with salary above 4000:", salary_above_4000)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Data Transformation for API Results
users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 30, "active": False},
    {"name": "Charlie", "age": 22, "active": True},
]

active_users = list(filter(lambda user: user['active'], users))
print("Active Users:", active_users)

user_names = list(map(lambda user: user['name'], users))
print("User Names:", user_names)

active_user_names = list(map(lambda user: user['name'], filter(lambda user: user['active'], users)))
print("Active User Names:", active_user_names)
