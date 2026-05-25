employees = [
    {"name":"A", "salary":30000},
    {"name":"B", "salary":50000},
    {"name":"C", "salary":40000}
]

max_salary = 0

for emp in employees:
    if emp["salary"] > max_salary:
        max_salary = emp["salary"]

print(max_salary)
