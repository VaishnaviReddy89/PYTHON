students = {
    "Alice": [80, 90, 85],
    "Bob": [70, 60, 75],
    "Charlie": [95, 85, 90]
}
 #AVERAGE MARKS
for name,marks in students.items():
     avg=sum(marks) / len(marks)
     print(name,"average:",avg)
