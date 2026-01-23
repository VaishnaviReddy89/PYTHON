print("+-------STUDENT MARKS PROCESSING-------+")
MARKS=input("ENTER STUDENTS MARKS: ")

print("ENTER CONVERSION TYPE")
print("1.YOU TO CONVERT TO INTEGER THEN CHOOSE THESE OPTION")
print("2.YOU TO CONVERT TO FLAOT THEN CHOOSE THESE OPTION")

choice=int(input("enter a choice: "))
if choice==1:
    print("INTEGER VALUE: ", int(float(MARKS)))
elif choice==2:
    print("FLOAT MARKS: ",float(MARKS))
else:
    print("YOU ARE CHOOSEN INVALID CHOICE SO PLEASE TRY AGAIN!!!!")
